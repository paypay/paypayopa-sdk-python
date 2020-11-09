import hmac
import hashlib
import base64
import json

import jwt
import requests
import uuid
import datetime

import pkg_resources
from pkg_resources import DistributionNotFound

from types import ModuleType
from .constants import URL, HTTP_STATUS_CODE

from . import resources


def capitalize_camel_case(string):
    return "".join(map(str.capitalize, string.split('_')))


# Create a dict of resource classes
RESOURCE_CLASSES = {}
for name, module in resources.__dict__.items():
    if isinstance(module, ModuleType) and \
            capitalize_camel_case(name) in module.__dict__:
        RESOURCE_CLASSES[capitalize_camel_case(name)] = module.__dict__[capitalize_camel_case(name)]


class Client:
    """PayPay client class"""
    DEFAULTS = {
        'sandbox_base_url': URL.SANDBOX_BASE_URL,
        'production_base_url': URL.PRODUCTION_BASE_URL
    }

    def __init__(self,
                 session=None,
                 auth=None,
                 production_mode=False,
                 **options):
        """
        Initialize a Client object with session,
        optional auth handler, and options
        """
        self.session = session or requests.Session()
        self.auth = auth
        self.production_mode = production_mode
        self.assume_merchant = ""

        self.base_url = self._set_base_url(**options)
        # intializes each resource
        # injecting this client object into the constructor
        for name, Klass in RESOURCE_CLASSES.items():
            setattr(self, name, Klass(self))

    def get_version(self):
        version = ""
        try:
            version = pkg_resources.require("paypayopa")[0].version
        except DistributionNotFound:
            print('DistributionNotFound')
        return version


    def _set_base_url(self, **options):
        if self.production_mode is False:
            base_url = self.DEFAULTS['sandbox_base_url']
        if self.production_mode is True:
            base_url = self.DEFAULTS['production_base_url']
        if 'base_url' in options:
            base_url = options['base_url']
            del (options['base_url'])
        return base_url

    def set_assume_merchant(self, merchant):
        if (merchant):
            self.assume_merchant = merchant

    def encode_jwt(self, secret=str, scope="direct_debit",
                   redirect_url=None,
                   reference_id=str(uuid.uuid4())[:8],
                   device_id="", phone_number=""):
        jwt_data = {
            "iss": 'merchant',
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
            "scope": scope,
            "nonce": str(uuid.uuid4())[:8],
            "redirectUrl": redirect_url,
            "referenceId": reference_id,
            "deviceId": device_id,
            "phoneNumber": phone_number
        }
        encoded = jwt.encode(jwt_data,
                             base64.b64decode(secret),
                             algorithm='HS256')
        return encoded

    def decode_jwt(self, secret, token):
        try:
            ca = jwt.decode(token, secret, verify=False)
            return ca.get('userAuthorizationId'), ca.get('referenceId')
        except Exception as e:
            print("JWT Signature verification failed: ", e)

    def auth_header(self, api_key, api_secret,
                    method, resource, content_type="empty",
                    request_body=None):
        auth_type = 'hmac OPA-Auth'
        nonce = str(uuid.uuid4())[:8]
        timestamp = str(int(datetime.datetime.now().timestamp()))
        body_hash = "empty"
        if request_body is not None:
            hashed_body = hashlib.md5()
            hashed_body.update(content_type.encode("utf-8"))
            hashed_body.update(request_body.encode("utf-8"))
            body_hash = base64.b64encode(hashed_body.digest())
        if body_hash != "empty":
            body_hash = body_hash.decode()
        signature_list = "\n".join([resource,
                                    method,
                                    nonce,
                                    timestamp,
                                    content_type,
                                    body_hash])
        hmac_data = hmac.new(api_secret.encode("utf-8"),
                             signature_list.encode("utf-8"),
                             digestmod=hashlib.sha256)
        hmac_base64 = base64.b64encode(hmac_data.digest())
        header_list = [api_key,
                       hmac_base64.decode("utf-8"),
                       nonce, timestamp,
                       body_hash]
        header = ":".join(header_list)
        return "{}:{}".format(auth_type, header)

    def request(self, method, path, auth_header, **options):
        """
        Dispatches a request to the PayPay HTTP API
        """
        api_name = options['api_id']
        del options['api_id']
        url = "{}{}".format(self.base_url, path)
        response = getattr(self.session, method)(url, headers={
            'Authorization': auth_header,
            'Content-Type': 'application/json;charset=UTF-8',
            'X-ASSUME-MERCHANT': self.assume_merchant
        }, **options)
        if ((response.status_code >= HTTP_STATUS_CODE.OK) and
                (response.status_code < HTTP_STATUS_CODE.REDIRECT)):
            return response.json()
        else:
            json_response = response.json()
            resolve_url = "{}?api_name={}&code={}&code_id={}".format(
                        URL.RESOLVE,
                        api_name,
                        json_response['resultInfo']['code'],
                        json_response['resultInfo']['codeId'])
            print("This link should help you to troubleshoot the error: " + resolve_url)
            return json_response

    def get(self, path, params, **options):
        """
        Parses GET request options and dispatches a request
        """
        method = "GET"
        data, auth_header = self._update_request(None, path, method)
        return self.request("get",
                            path,
                            params=params,
                            auth_header=auth_header,
                            **options)

    def post(self, path, data, **options):
        """
        Parses POST request options and dispatches a request
        """
        method = "POST"
        data, auth_header = self._update_request(data, path, method)
        return self.request("post",
                            path,
                            data=data,
                            auth_header=auth_header,
                            **options)

    def patch(self, path, data, **options):
        """
        Parses PATCH request options and dispatches a request
        """
        method = "PATCH"
        data, auth_header = self._update_request(data, path, method)
        return self.request("patch",
                            path,
                            auth_header=auth_header,
                            **options)

    def delete(self, path, data, **options):
        """
        Parses DELETE request options and dispatches a request
        """
        method = "DELETE"
        data, auth_header = self._update_request(data, path, method)
        return self.request("delete",
                            path,
                            data=data,
                            auth_header=auth_header,
                            **options)

    def put(self, path, data, **options):
        """
        Parses PUT request options and dispatches a request
        """
        method = "PUT"
        data, auth_header = self._update_request(data, path, method)
        return self.request("put",
                            path,
                            data=data,
                            auth_header=auth_header,
                            **options)

    def _update_request(self, data, path, method):
        """
        Updates The resource data and header options
        """
        _data = None
        content_type = "empty"
        if data is not None:
            _data = json.dumps(data)
            content_type = "application/json;charset=UTF-8"
        uri_path = path
        _auth_header = self.auth_header(
            self.auth[0],
            self.auth[1],
            method,
            uri_path,
            content_type,
            _data)
        return _data, _auth_header

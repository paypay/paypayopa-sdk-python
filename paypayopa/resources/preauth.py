from .base import Resource
from ..constants.url import URL
from ..constants.api_list import API_NAMES
import datetime


class Preauth(Resource):
    def __init__(self, client=None):
        super(Preauth, self).__init__(client)
        self.base_url = URL.PAYMENT

    def pre_authorize_create(self, data={}, **kwargs):
        url = "{}/{}".format(self.base_url, 'preauthorize')
        if "requestedAt" not in data:
            data['requestedAt'] = int(datetime.datetime.now().timestamp())
        if "merchantPaymentId" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for merchantPaymentId")
        if "userAuthorizationId" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for merchantPaymentId")
        if "amount" not in data["amount"]:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for amount")
        if type(data["expiresAt"]) != int:
            raise ValueError("\x1b[31m expiresAt should be of "
                             "type integer (EPOCH) \x1b[0m")
        if type(data["amount"]["amount"]) != int:
            raise ValueError("\x1b[31m Amount should be of type integer"
                             " \x1b[0m")
        if "currency" not in data["amount"]:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for currency")
        return self.post_url(url, data, api_id=API_NAMES.PREAUTHORIZE_PAYMENT, **kwargs)

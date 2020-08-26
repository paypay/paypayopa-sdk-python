from .base import Resource
from ..constants.url import URL
import datetime


class PreAuthorize(Resource):
    def __init__(self, client=None):
        super(PreAuthorize, self).__init__(client)
        self.base_url = URL.PAYMENT

    def create(self, data={}, **kwargs):
        url = "{}/{}".format(self.base_url, 'preauthorize')
        if "requestedAt" not in data:
            data['requestedAt'] = int(datetime.datetime.now().timestamp())
        if "merchantPaymentId" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for merchantPaymentId")
        if "userAuthorizationId" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for merchantPaymentId")
        if "userAuthorizationId" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for userAuthorizationId")
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
        return self.post_url(url, data, **kwargs)

    def get_payment_details(self, id, **kwargs):
        url = "{}/{}".format(self.base_url, id)
        if id is None:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for merchantPaymentId")
        return self.fetch(None, url, **kwargs)

    def cancel_payment(self, id, **kwargs):
        url = "{}/{}".format(self.base_url, id)
        if id is None:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for merchantPaymentId")
        return self.delete(None, url, **kwargs)

    def capture(self, data={}, **kwargs):
        url = "{}/{}".format(self.base_url, 'capture')
        if "requestedAt" not in data:
            data['requestedAt'] = int(datetime.datetime.now().timestamp())
        if "merchantPaymentId" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for merchantPaymentId")
        if "merchantCaptureId" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for merchantCaptureId")
        if "orderDescription" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for orderDescription")
        if "amount" not in data["amount"]:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for amount")
        if type(data["amount"]["amount"]) != int:
            raise ValueError("\x1b[31m Amount should be of type integer"
                             " \x1b[0m")
        if "currency" not in data["amount"]:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for currency")
        return self.post_url(url, data, **kwargs)

    def revert_payment(self, data={}, **kwargs):
        url = "{}/{}/{}".format(self.base_url, 'preauthorize', 'revert')
        if "requestedAt" not in data:
            data['requestedAt'] = int(datetime.datetime.now().timestamp())
        if "merchantRevertId" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for merchantPaymentId")
        if "paymentId" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for merchantPaymentId")
        return self.post_url(url, data, **kwargs)

    def refund_payment(self, data={}, **kwargs):
        url = "{}".format('/v2/refunds')
        if "requestedAt" not in data:
            data['requestedAt'] = datetime.datetime.now().second
        if "merchantPaymentId" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for merchantPaymentId")
        if "userAuthorizationId" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for userAuthorizationId")
        if "amount" not in data["amount"]:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for amount")
        if type(data["amount"]["amount"]) != int:
            raise ValueError("\x1b[31m Amount should be of type integer"
                             " \x1b[0m")
        if "currency" not in data["amount"]:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for currency")
        return self.post_url(url, data, **kwargs)

    def refund_details(self, id=None, **kwargs):
        if id is None:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for merchantRefundId")
        url = "{}/{}".format('/v2/refunds', id)
        return self.fetch(None, url, **kwargs)

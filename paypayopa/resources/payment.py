from .base import Resource
from ..constants.url import URL
from ..constants.api_list import API_NAMES
import datetime


class Payment(Resource):
    def __init__(self, client=None):
        super(Payment, self).__init__(client)
        self.base_url = URL.PAYMENT

    def create(self, data={}, **kwargs):
        url = "{}/{}".format(self.base_url, 'payments')
        if "requestedAt" not in data:
            data['requestedAt'] = int(datetime.datetime.now().timestamp())
        if "merchantPaymentId" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for merchantPaymentId")
        if "amount" not in data["amount"]:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for amount")
        if type(data["amount"]["amount"]) != int:
            raise ValueError("\x1b[31m Amount should be of type integer"
                             " \x1b[0m")
        if "currency" not in data["amount"]:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for currency")
        return self.post_url(url, data, api_id=API_NAMES.CREATE_PAYMENT, **kwargs)

    def get_payment_details(self, id, **kwargs):
        url = "{}/{}".format(self.base_url, id)
        if id is None:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for merchantPaymentId")
        return self.fetch(None, url, None, api_id=API_NAMES.GET_PAYMENT, **kwargs)

    def cancel_payment(self, id, **kwargs):
        url = "{}/{}".format(self.base_url, id)
        if id is None:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for merchantPaymentId")
        return self.delete(None, url, None, api_id=API_NAMES.CANCEL_PAYMENT, **kwargs)

    def refund_payment(self, data={}, **kwargs):
        url = "{}/".format('/v2/refunds')
        if "requestedAt" not in data:
            data['requestedAt'] = datetime.datetime.now().second
        if "merchantPaymentId" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for merchantPaymentId")
        if "paymentId" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for paymentId")
        if "amount" not in data["amount"]:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for amount")
        if type(data["amount"]["amount"]) != int:
            raise ValueError("\x1b[31m Amount should be of type integer"
                             " \x1b[0m")
        if "currency" not in data["amount"]:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for currency")
        return self.post_url(url, data, api_id=API_NAMES.REFUND_PAYMENT, **kwargs)

    def refund_details(self, id=None, **kwargs):
        if id is None:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for merchantRefundId")
        url = "{}/{}".format('/v2/refunds', id)
        return self.fetch(None, url, None, api_id=API_NAMES.GET_REFUND, **kwargs)

    def capture_payment(self, data=None, **kwargs):
        if data is None:
            data = {}
        url = "{}/{}".format('/v2/payments', 'capture')
        if "requestedAt" not in data:
            data['requestedAt'] = int(datetime.datetime.now().timestamp())
        if "merchantPaymentId" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for merchantPaymentId")
        if "merchantCaptureId" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for merchantPaymentId")
        if "orderDescription" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for merchantPaymentId")
        if "amount" not in data["amount"]:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for amount")
        if type(data["amount"]["amount"]) != int:
            raise ValueError("\x1b[31m Amount should be of type integer"
                             " \x1b[0m")
        if "currency" not in data["amount"]:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for currency")
        return self.post_url(url, data, api_id=API_NAMES.CAPTURE_PAYMENT, **kwargs)

    def create_continuous_payment(self, data=None, **kwargs):
        if data is None:
            data = {}
        url = "{}/{}".format('/v1/subscription', 'payments')
        if "requestedAt" not in data:
            data['requestedAt'] = int(datetime.datetime.now().timestamp())
        if "merchantPaymentId" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for merchantPaymentId")
        if "userAuthorizationId" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for userAuthorizationId")
        if "amount" not in data["amount"]:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for amount")
        if type(data["amount"]["amount"]) != int:
            raise ValueError("\x1b[31m Amount should be of type integer"
                             " \x1b[0m")
        if "currency" not in data["amount"]:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for currency")
        return self.post_url(url, data,  api_id=API_NAMES.CREATE_CONTINUOUS_PAYMENT,  **kwargs)

    def revert_payment(self, data=None, **kwargs):
        if data is None:
            data = {}
        url = "{}/{}/{}".format('/v2/payments', 'preauthorize', 'revert')
        if "requestedAt" not in data:
            data['requestedAt'] = int(datetime.datetime.now().timestamp())
        if "merchantRevertId" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for merchantPaymentId")
        if "paymentId" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for merchantPaymentId")
        return self.post_url(url, data, api_id=API_NAMES.REVERT_AUTHORIZE, **kwargs)

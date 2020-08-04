from .base import Resource
from ..constants.url import URL
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

    def get_payment_details(self, id, **kwargs):
        url = "{}/{}/{}".format(self.base_url, 'payments', id)
        if id is None:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for merchantPaymentId")
        return self.fetch(None, url, **kwargs)

    def cancel_payment(self, id, **kwargs):
        url = "{}/{}".format('payments', id)
        if id is None:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for merchantPaymentId")
        return self.delete(None, url, **kwargs)

    def refund_payment(self, data={}, **kwargs):
        url = "/{}".format('refunds')
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

    def refund_details(self, data={}, **kwargs):
        if id is None:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for merchantRefundId")
        url = "/{}".format('refunds')
        return self.fetch(url, data, **kwargs)

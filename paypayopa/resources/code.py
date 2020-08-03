from .base import Resource
from ..constants.url import URL
import datetime


class Code(Resource):
    def __init__(self, client=None):
        super(Code, self).__init__(client)
        self.base_url = URL.CODE

    def create_qr_code(self, data={}, **kwargs):
        url = self.base_url
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
        for item in data["orderItems"]:
            if "name" not in item:
                raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                                 " \x1b[0m for orderItem Name")
            if "quantity" not in item:
                raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                                 " \x1b[0m for orderItem quantity")
            if "amount" not in item["unitPrice"]:
                raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                                 " \x1b[0m for orderItem.amount.unitPrice")
            if "currency" not in item["unitPrice"]:
                raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                                 " \x1b[0m for orderItem.amount.currency")
        return self.post_url(url, data, **kwargs)

    def delete_qr_code(self, id=None, **kwargs):
        if id is None:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for codeId")
        return self.delete(id)

    def get_payment_details(self, id=None, **kwargs):
        if id is None:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for merchantPaymentId")
        url = "{}/{}/{}".format(self.base_url, 'payments', id)
        return self.fetch(None, url, **kwargs)

    def cancel_payment(self, id=None, **kwargs):
        if id is None:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for merchantPaymentId")
        url = "{}/{}".format('payments', id)
        return self.delete(None, url, **kwargs)

    def capture_payment(self, data={}, **kwargs):
        url = "{}/{}".format('payments', 'capture')
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
        return self.post_url(url, data, **kwargs)

    def revert_payment(self, data={}, **kwargs):
        url = "{}/{}/{}".format('payments', 'preauthorize', 'revert')
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
        url = "/{}".format('refunds')
        if "requestedAt" not in data:
            data['requestedAt'] = int(datetime.datetime.now().timestamp())
        if "merchantRefundId" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for merchantPaymentId")
        if "paymentId" not in data:
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
        return self.post_url(url, data, **kwargs)

    def refund_details(self, id=None, **kwargs):
        if id is None:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for merchantRefundId")
        url = "/{}/{}".format('refunds', id)
        return self.fetch(None, url, **kwargs)

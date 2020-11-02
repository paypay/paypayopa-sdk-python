from ..resources.base import Resource
from ..constants.url import URL
from ..constants.api_list import API_NAMES
import datetime

class Code(Resource):
    def __init__(self, client=None):
        super(Code, self).__init__(client)
        Code.base_url = URL.CODE

    def create_qr_code(self, data=None, **kwargs):
        if data is None:
            data = {}
        url = self.base_url
        if "requestedAt" not in data:
            data["requestedAt"] = int(datetime.datetime.now().timestamp())
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
        return self.post_url(url, data, api_id=API_NAMES.CREATE_QRCODE, **kwargs)

    def get_payment_details(self, id, **kwargs):
        url = "{}/{}/{}".format(self.base_url, 'payments', id)
        if id is None:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for merchantPaymentId")
        return self.fetch(None, url, None, api_id=API_NAMES.GET_QR_PAYMENT, **kwargs)

    def delete_qr_code(self, id=None, **kwargs):
        if id is None:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for codeId")
        url = "{}/{}".format(self.base_url, id)
        return self.delete(None, url, api_id=API_NAMES.DELETE_QRCODE, **kwargs)

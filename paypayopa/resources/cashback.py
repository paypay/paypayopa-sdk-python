from ..resources.base import Resource
from ..constants.url import URL
from ..constants.api_list import API_NAMES


class Cashback(Resource):
    def __init__(self, client=None):
        super(Cashback, self).__init__(client)
        self.give_base_url = URL.GIVE_CASHBACK
        self.reverse_base_url = URL.REVERSAL_CASHBACK

    def give_cashback(self, data=None, **kwargs):
        if data is None:
            data = {}
        url = "{}".format(self.give_base_url)
        if "merchantCashbackId" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for merchantCashbackId")
        if "userAuthorizationId" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for userAuthorizationId")
        if "amount" not in data["amount"]:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for amount amount")
        if "currency" not in data["amount"]:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for amount currency")
        if "requestedAt" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for requestedAt")
        if "walletType" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for walletType")
        return self.post_url(url, data, api_id=API_NAMES.CREATE_CASHBACK_REQUEST, **kwargs)

    def check_cashback_detail(self, merchant_cashback_id, **kwargs):
        if merchant_cashback_id is None:
            raise ValueError("\x1b[31m MISSING merchantCashbackId")
        url = "{}/{}".format(self.give_base_url, merchant_cashback_id)
        return self.get_url(url=url, data={}, api_id=API_NAMES.GET_CASHBACK_DETAILS, **kwargs)

    def reverse_cashback(self, data=None, **kwargs):
        if data is None:
            data = {}
        url = "{}".format(self.reverse_base_url)
        if "merchantCashbackReversalId" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for merchantCashbackReversalId")
        if "merchantCashbackId" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for merchantCashbackId")
        if "amount" not in data["amount"]:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for amount amount")
        if "currency" not in data["amount"]:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for amount currency")
        if "requestedAt" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for requestedAt")
        return self.post_url(url, data, api_id=API_NAMES.CREATE_REVERSE_CASHBACK_REQUEST, **kwargs)

    def check_cashback_reversal_detail(self, merchant_cashback_reversal_id=None, merchant_cashback_id=None, **kwargs):
        url = "{}/{}/{}".format(self.reverse_base_url, merchant_cashback_reversal_id, merchant_cashback_id)
        if merchant_cashback_reversal_id is None:
            raise ValueError("\x1b[31m MISSING merchantCashbackReversalId")
        if merchant_cashback_id is None:
            raise ValueError("\x1b[31m MISSING merchantCashbackId")
        return self.get_url(url=url, data={}, api_id=API_NAMES.GET_REVERESED_CASHBACK_DETAILS, **kwargs)

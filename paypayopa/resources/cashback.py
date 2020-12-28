from ..resources.base import Resource
from ..constants.url import URL
from ..constants.api_list import API_NAMES


class Cashback(Resource):
    def __init__(self, client=None):
        super(Cashback, self).__init__(client)
        self.give_base_url = URL.GIVE_CASHBACK
        self.reverse_base_url = URL.REVERSE_CASHBACK

    def give_cashback(self, data, **kwargs):
        if data is None:
            data = {}
        url = "{}".format(self.give_base_url)
        return self.post_url(url, data, api_id=API_NAMES.GIVE_CASHBACK, **kwargs)

    def check_give_cashback(self, merchant_cashback_id, **kwargs):
        if merchant_cashback_id is None:
            raise ValueError("\x1b[31m MISSING MerchantCashbackId")
        url = "{}/{}".format(self.give_base_url, merchant_cashback_id)
        return self.get_url(url, api_id=API_NAMES.GIVE_CASHBACK, **kwargs)

    def reverse_cashback(self, data, **kwargs):
        if data is None:
            data = {}
        url = "{}".format(self.reverse_base_url)
        return self.post_url(url, data, api_id=API_NAMES.REVERSE_CASHBACK, **kwargs)

    def check_reverse_cashback(self, merchant_cashback_reversal_id, merchant_cashback_id, data, **kwargs):
        if merchant_cashback_reversal_id is None:
            raise ValueError("\x1b[31m MISSING merchantCashbackReversalId")
        if merchant_cashback_id is None:
            raise ValueError("\x1b[31m MISSING MerchantCashbackId")
        url = "{}/{}".format(self.reverse_base_url, merchant_cashback_id)
        return self.get_url(url, api_id=API_NAMES.REVERSE_CASHBACK, **kwargs)


from ..resources.base import Resource
from ..constants.url import URL
from ..constants.api_list import API_NAMES


class Cashback(Resource):
    def __init__(self, client=None):
        super(Cashback, self).__init__(client)
        self.give_base_url = URL.GIVE_CASHBACK

    def give_cashback(self, data, **kwargs):
        if data is None:
            data = {}
        url = "{}".format(self.give_base_url)
        return self.post_url(url, data, api_id=API_NAMES.GIVE_CASHBACK, **kwargs)

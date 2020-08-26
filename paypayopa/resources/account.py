from .base import Resource
from ..constants.url import URL


class Account(Resource):
    def __init__(self, client=None):
        super(Account, self).__init__(client)
        self.base_url = URL.ACCOUNT_LINK

    def create_qr_session(self, data={}, **kwargs):
        url = self.base_url
        if "scopes" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for scopes")
        if "nonce" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for nonce")
        if "redirectUrl" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for redirectUrl")
        if "referenceId" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for referenceId")
        return self.post_url(url, data, **kwargs)

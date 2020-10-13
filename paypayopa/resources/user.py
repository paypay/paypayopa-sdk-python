from ..resources.base import Resource
from ..constants.url import URL


class User(Resource):
    def __init__(self, client=None):
        super(User, self).__init__(client)
        User.base_url = URL.USER_AUTH

    def get_authorization_status(self, id, **kwargs):
        url = self.base_url
        params = {
            "userAuthorizationId": id
        }
        if id is None:
            raise ValueError("\x1b[31m MISSING QUERY PARAM"
                             " \x1b[0m for userAuthorizationId")
        return self.fetch(None, url, params, **kwargs)

    def unlink_user_athorization(self, id=None, **kwargs):
        if id is None:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for codeId")
        url = "{}/{}".format(self.base_url, id)
        return self.delete(None, url, **kwargs)

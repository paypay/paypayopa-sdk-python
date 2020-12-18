import responses
import json

from .helpers import mock_file, ClientTestCase


class TestGetUserAuthStatus(ClientTestCase):

    def setUp(self):
        super(TestGetUserAuthStatus, self).setUp()
        self.base_url = '{}/user/authorizations?userAuthorizationId=fakeid'.format(
            self.base_url)

    @responses.activate
    def test_get_user_auth_status(self):
        """Test user auth status."""
        result = mock_file('get_user_auth_status')
        # url = '{}/{}'.format(self.base_url, 'fake_userId')
        url = self.base_url
        params = {
            "fakeid": 'fakeid'
        }
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True, )
        self.assertEqual(
            self.client.User.get_authorization_status(params), result)

import responses
import json

from .helpers import mock_file, ClientTestCase


class TestUnLinkUser(ClientTestCase):

    def setUp(self):
        super(TestUnLinkUser, self).setUp()
        self.base_url = '{}/user/authorizations'.format(
            self.base_url)

    @responses.activate
    def test_unlink_user(self):
        """Test UnLink user."""
        result = mock_file('unlink_user')
        url = '{}/{}'.format(self.base_url, 'fake_userId')
        responses.add(responses.DELETE, url, status=200, body=json.dumps(result),
                      match_querystring=True, )
        self.assertEqual(
            self.client.User.unlink_user_athorization('fake_userId'), result)

import responses
import json

from .helpers import mock_file, ClientTestCase


class TestUnlinkUser(ClientTestCase):

    def setUp(self):
        super(TestUnlinkUser, self).setUp()
        self.base_url = '{}/user/authorizations/fake_user_id'.format(
            self.base_url)

    @responses.activate
    def test_unlink_user(self):
        fake_user_id = 1234
        result = mock_file('unlink_user')
        url = "{}/{}".format(self.base_url, fake_user_id)
        responses.add(responses.DELETE, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.User.unlink_user_athorization(
            fake_user_id), result)

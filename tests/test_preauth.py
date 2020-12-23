import responses
import json

from .helpers import mock_file, ClientTestCase


class TestPreAuth(ClientTestCase):

    def setUp(self):
        super(TestPreAuth, self).setUp()
        self.base_url = '{}/payments/preauthorize'.format(self.base_url)

    @responses.activate
    def test_preauth(self):
        """Test preauth."""
        init = mock_file('preauth_payload')
        result = mock_file('preauth_response')
        url = self.base_url
        # url = "{}/{}".format(self.base_url, 'preauthorize')
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(
            self.client.Preauth.pre_authorize_create(init), result)

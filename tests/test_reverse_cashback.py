import json
import responses

from .helpers import mock_file, ClientTestCase


class TestReversesCashback(ClientTestCase):

    def setUp(self):
        super(TestReversesCashback, self).setUp()
        self.base_url = '{}/cashback_reversal'.format(self.base_url)

    @responses.activate
    def test_reverse_cashback(self):
        """ Test reverse cashback """
        init = mock_file('reverse_cashback_payload')
        result = mock_file('reverse_cashback_response')
        url = self.base_url
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.Cashback.reverse_cashback(init), result)

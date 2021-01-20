import json
import responses

from .helpers import mock_file, ClientTestCase


class TestGiveCashback(ClientTestCase):

    def setUp(self):
        super(TestGiveCashback, self).setUp()
        self.base_url = '{}/cashback'.format(self.base_url)

    @responses.activate
    def test_give_cashback(self):
        """ Test give cashback"""
        init = mock_file('give_cashback_payload')
        result = mock_file('give_cashback_response')
        url = self.base_url
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.Cashback.give_cashback(init), result)

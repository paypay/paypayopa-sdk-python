import json
import responses

from .helpers import mock_file, ClientTestCase


class TestCheckCashbackDetail(ClientTestCase):

    def setUp(self):
        super(TestCheckCashbackDetail, self).setUp()
        self.base_url = '{}/cashback'.format(self.base_url)

    @responses.activate
    def test_check_cashback_detail(self):
        """ Test check cashback detail """
        init = 'fake_merchant_cashback_id'
        result = mock_file('check_cashback_detail_response')
        url = '{}/{}'.format(self.base_url, init)
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.Cashback.check_cashback_detail(init), result)

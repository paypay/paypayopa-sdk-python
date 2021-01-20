import json
import responses

from .helpers import mock_file, ClientTestCase


class TestCheckCashbackReversalDetails(ClientTestCase):

    def setUp(self):
        super(TestCheckCashbackReversalDetails, self).setUp()
        self.base_url = '{}/cashback_reversal'.format(self.base_url)

    @responses.activate
    def test_check_cashback_reversal_detail(self):
        """ Test check cashback reversal detail """
        cashback_reversal_id = 'fake_merchant_cashback_reversal_id'
        cashback_id = 'fake_merchant_cashback_id'
        result = mock_file('check_cashback_reversal_details_response')
        url = '{}/{}/{}'.format(self.base_url, cashback_reversal_id, cashback_id)
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.Cashback.check_cashback_reversal_detail(cashback_reversal_id,
                                                                             cashback_id),
                         result)

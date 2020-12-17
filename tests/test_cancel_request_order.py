import responses
import json

from .helpers import mock_file, ClientTestCase


class TestCancelRequestOrder(ClientTestCase):

    def setUp(self):
        super(TestCancelRequestOrder, self).setUp()
        self.base_url = '{}/requestOrder/fakeMerchantId'.format(self.base_url)

    @responses.activate
    def test_test_cancel_request_order(self):
        """Test cancel request order"""

        result = mock_file('cancel_request_order_response')
        url = "https://stg-api.sandbox.paypay.ne.jp/v1/requestOrder/fakeMerchantId"
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True, )
        self.assertEqual(
            self.client.Pending.refund_details('fakeMerchantId'), result)

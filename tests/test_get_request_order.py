import responses
import json

from .helpers import mock_file, ClientTestCase


class TestGetRequestOrder(ClientTestCase):

    def setUp(self):
        super(TestGetRequestOrder, self).setUp()
        self.base_url = '{}/requestOrder/fake_merchant_payment_id'.format(
            self.base_url)

    @responses.activate
    def test_get_request_order(self):
        """Test get request order."""
        result = mock_file('get_request_order_response')
        url = "https://stg-api.sandbox.paypay.ne.jp/v1/requestOrder/fake_merchant_payment_id"
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.Pending.get_payment_details(
            'fake_merchant_payment_id'), result)

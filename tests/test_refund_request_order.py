import responses
import json

from .helpers import mock_file, ClientTestCase


class TestRefundRequestOrder(ClientTestCase):

    def setUp(self):
        super(TestRefundRequestOrder, self).setUp()
        self.base_url = '{}/requestOrder/refunds/'.format(self.base_url)

    @responses.activate
    def test_refund_request_order(self):
        """Test refund request order"""
        init = mock_file('refund_request_order_payload')
        result = mock_file('refund_request_order_response')
        url = "https://stg-api.sandbox.paypay.ne.jp/v1/requestOrder/refunds"
        responses.add(responses.POST, url, status=200, body=json.dumps(result))
        self.assertEqual(self.client.Pending.refund_payment(init), result)

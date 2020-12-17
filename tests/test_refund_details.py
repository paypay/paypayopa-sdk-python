import responses
import json

from .helpers import mock_file, ClientTestCase


class TestRefundDetails(ClientTestCase):

    def setUp(self):
        super(TestRefundDetails, self).setUp()
        self.base_url = '{}/refunds/fake_merchant_refundId'.format(
            self.base_url)

    @responses.activate
    def test_refund_details(self):
        """
        Test refund details.
        """
        result = mock_file('refund_details')
        url = self.base_url
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.Payment.refund_details(
            'fake_merchant_refundId'), result)

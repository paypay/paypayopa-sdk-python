import responses
import json

from .helpers import mock_file, ClientTestCase


class TestRefundPayment(ClientTestCase):

    def setUp(self):
        super(TestRefundPayment, self).setUp()
        self.base_url = '{}/refunds/'.format(self.base_url)

    @responses.activate
    def test_refund_payment(self):
        """
        Test refund payment
        """
        init = mock_file('refund_payment_payload')
        result = mock_file('refund_payment_response')
        url = self.base_url
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.Payment.refund_payment(init), result)

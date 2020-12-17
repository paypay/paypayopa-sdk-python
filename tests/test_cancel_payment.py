import responses
import json

from .helpers import mock_file, ClientTestCase


class TestCancelPayment(ClientTestCase):

    def setUp(self):
        super(TestCancelPayment, self).setUp()
        self.base_url = '{}/payments/fake_merchant_payment_id'.format(
            self.base_url)

    @responses.activate
    def test_cancel_payment(self):
        """
            Test cancel payment
        """
        result = mock_file('cancel_payment')
        url = self.base_url
        responses.add(responses.DELETE, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.Payment.cancel_payment(
            'fake_merchant_payment_id'), result)

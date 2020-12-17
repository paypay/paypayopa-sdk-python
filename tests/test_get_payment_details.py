import responses
import json

from .helpers import mock_file, ClientTestCase


class TestGetPaymentDetails(ClientTestCase):

    def setUp(self):
        super(TestGetPaymentDetails, self).setUp()
        self.base_url = '{}/payments/fake_merchant_payment_id'.format(
            self.base_url)

    @responses.activate
    def test_get_payment_details(self):
        """
        Test get payment details.
        """
        result = mock_file('get_payment_details')
        url = self.base_url
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.Payment.get_payment_details(
            'fake_merchant_payment_id'), result)

import responses
import json

from .helpers import mock_file, ClientTestCase


class TestCreateContinuesPayment(ClientTestCase):

    def setUp(self):
        super(TestCreateContinuesPayment, self).setUp()

    @responses.activate
    def test_CreateContinuesPayment(self):
        """
            Test create continues payment.
        """
        init = mock_file('create_continues_payment_payload')
        result = mock_file('create_continues_payment_response')
        url = "https://stg-api.sandbox.paypay.ne.jp/v1/subscription/payments"
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(
            self.client.Payment.create_continuous_payment(init), result)

import responses
import json

from .helpers import mock_file, ClientTestCase


class TestCapturePayment(ClientTestCase):

    def setUp(self):
        super(TestCapturePayment, self).setUp()
        self.base_url = '{}/payments/capture'.format(
            self.base_url)

    @responses.activate
    def testcapture_payment(self):
        """
            Test capture payment
        """
        init = mock_file('capture_payment_payload')
        result = mock_file('capture_payment_response')
        url = self.base_url
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.Payment.capture_payment(init), result)

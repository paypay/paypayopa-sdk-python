import responses
import json

from .helpers import mock_file, ClientTestCase


class TestCreatePayment(ClientTestCase):

    def setUp(self):
        super(TestCreatePayment, self).setUp()
        self.base_url = '{}/payments'.format(self.base_url)

    @responses.activate
    def test_create_payment(self):
        """Test create payment."""
        init = mock_file('create_payment_payload')
        result = mock_file('create_payment_response')
        url = url = "{}/{}".format(self.base_url, 'payments')
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.Payment.create(init), result)

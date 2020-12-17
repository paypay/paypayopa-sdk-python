import responses
import json

from .helpers import mock_file, ClientTestCase


class TestRevertPayment(ClientTestCase):

    def setUp(self):
        super(TestRevertPayment, self).setUp()
        self.base_url = '{}/payments/preauthorize/revert'.format(
            self.base_url)

    @responses.activate
    def test_revert_payment(self):
        """Test revert payment."""
        init = mock_file('revert_payment_payload')
        result = mock_file('revert_payment_response')
        url = self.base_url
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.Payment.revert_payment(init), result)

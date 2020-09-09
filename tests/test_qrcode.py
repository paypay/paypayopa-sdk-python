import responses
import json

from .helpers import mock_file, ClientTestCase


class TestClientQRCode(ClientTestCase):

    def setUp(self):
        super(TestClientQRCode, self).setUp()
        self.base_url = '{}/codes'.format(self.base_url)

    @responses.activate
    def test_order_create(self):
        init = mock_file('create_qrcode')
        result = mock_file('create_qrcode_response')
        url = self.base_url
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.Code.create_qr_code(init), result)

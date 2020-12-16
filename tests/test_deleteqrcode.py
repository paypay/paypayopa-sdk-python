import responses
import json

from .helpers import mock_file, ClientTestCase


class TestDeleteQRCode(ClientTestCase):

    def setUp(self):
        super(TestDeleteQRCode, self).setUp()
        self.base_url = '{}/codes'.format(self.base_url)

    @responses.activate
    def test_qrcode_delete(self):
        result = mock_file('delete_qrcode')
        url = '{}/{}'.format(self.base_url, 'fake_qr_id')
        responses.add(responses.DELETE, url, status=200, body=json.dumps(result),
                      match_querystring=True, )
        self.assertEqual(self.client.Code.delete_qr_code('fake_qr_id'), result)

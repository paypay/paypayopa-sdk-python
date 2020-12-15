import responses
import json

from .helpers import mock_file, ClientTestCase


class TestDeleteQRCode(ClientTestCase):

    def setUp(self):
        super(TestDeleteQRCode, self).setUp()
        self.base_url = '{}/codes/test_id'.format(self.base_url)

    @responses.activate
    def test_qrcode_delete(self):
        result = mock_file('delete_qrcode')
        url = self.base_url
        responses.add(responses.DELETE, url, status=200)
        self.assertEqual(responses, result)

import responses
import json

from .helpers import mock_file, ClientTestCase


class TestCreateRequestOrder(ClientTestCase):

    def setUp(self):
        super(TestCreateRequestOrder, self).setUp()

    @responses.activate
    def test_TestCreateRequestOrder(self):
        init = mock_file('request_order_payload')
        result = mock_file('request_order_response')
        url = "https://stg-api.sandbox.paypay.ne.jp/v1/requestOrder"
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(
            self.client.Pending.create_pending_payment(init), result)

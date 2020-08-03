import paypayopa
import os
import unittest
import json


def mock_file(filename):
    if not filename:
        return ''
    file_dir = os.path.dirname(__file__)
    file_path = "{}/mocks/{}.json".format(file_dir, filename)
    return json.loads(open(file_path).read())


class ClientTestCase(unittest.TestCase):
    def setUp(self):
        self.base_url = 'https://stg-api.sandbox.paypay.ne.jp/v2'
        self.payment_id = 'fake_payment_id'
        self.refund_id = 'fake_refund_id'
        self.merchant_id = 'fake_merchant_id'
        self.client = paypayopa.Client(auth=('key_id', 'key_secret'))
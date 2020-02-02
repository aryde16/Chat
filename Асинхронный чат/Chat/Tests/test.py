import unittest
from get_data import get_post

class TestGetData(unittest.TestCase):
    def text_get_post(self):
        resp = get_post()
        self.assertIsInstance(resp, dict)
        self.assertTrue(resp)

unittest.main()

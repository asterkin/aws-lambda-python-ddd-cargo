import unittest
from lambda_handler import lambda_handler

class TestMate(unittest.TestCase):
    def test_handler(self):
        self.assertEqual('ABC', lambda_handler({'cargo': 'ABC'}, None))

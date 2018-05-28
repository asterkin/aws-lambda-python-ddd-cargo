from checkVoyage import lambda_handler
import unittest

class TestVyageChecking(unittest.TestCase):
    def test(self):
        self.assertEqual('EVENT_TYPE_IS_MISSING', lambda_handler({}, None))
        self.assertEqual('OK', lambda_handler({'eventType': 'RECEIVE'}, None))
        self.assertEqual('UNEXPECTED_VOYAGE_REFERENCE', lambda_handler({'eventType': 'RECEIVE', 'voyage': 'XYZ'}, None))
        self.assertEqual('VOYAGE_REF_IS_MISSING', lambda_handler({'eventType': 'LOAD'}, None))
        self.assertEqual('VOYAGE_REF_IS_MISSING', lambda_handler({'eventType': 'UNLOAD'}, None))
        self.assertEqual('OK', lambda_handler({'eventType': 'LOAD', 'voyage': 'XYZ'}, None))

if __name__ == '__main__':
    unittest.main()

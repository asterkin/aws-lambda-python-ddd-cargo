from calculateTransportationStatus import lambda_handler
import unittest

class TestTransportationStatus(unittest.TestCase):
    def test(self):
        self.assertEqual('NOT_RECEIVED', lambda_handler({}, None))
        self.assertEqual('UNKNOWN', lambda_handler({'eventType': 'KKK'}, None))
        self.assertEqual('IN_PORT', lambda_handler({'eventType': 'RECEIVE'}, None))
        self.assertEqual('ONBOARD_CARRIER', lambda_handler({'eventType': 'LOAD'}, None))
        self.assertEqual('IN_PORT', lambda_handler({'eventType': 'UNLOAD'}, None))
        self.assertEqual('IN_PORT', lambda_handler({'eventType': 'CUSTOMS'}, None))
        self.assertEqual('CLAIMED', lambda_handler({'eventType': 'CLAIM'}, None))

if __name__ == '__main__':
    unittest.main()


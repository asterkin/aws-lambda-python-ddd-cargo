from calculateTransportationStatus import calculateTransportationStatus
from mattea.jso import jso
import unittest

class TestTransportationStatus(unittest.TestCase):
    def test(self):
        self.assertEqual('NOT_RECEIVED', calculateTransportationStatus(jso({})))
        self.assertEqual('UNKNOWN', calculateTransportationStatus(jso({'eventType': 'KKK'})))
        self.assertEqual('IN_PORT', calculateTransportationStatus(jso({'eventType': 'RECEIVE'})))
        self.assertEqual('ONBOARD_CARRIER', calculateTransportationStatus(jso({'eventType': 'LOAD'})))
        self.assertEqual('IN_PORT', calculateTransportationStatus(jso({'eventType': 'UNLOAD'})))
        self.assertEqual('IN_PORT', calculateTransportationStatus(jso({'eventType': 'CUSTOMS'})))
        self.assertEqual('CLAIMED', calculateTransportationStatus(jso({'eventType': 'CLAIM'})))

if __name__ == '__main__':
    unittest.main()


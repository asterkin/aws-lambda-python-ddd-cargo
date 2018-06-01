from calculate_transportation_status import calculate_transportation_status
from matte.jso import jso
import unittest

class TestTransportationStatus(unittest.TestCase):
    def test(self):
        self.assertEqual('NOT_RECEIVED', calculate_transportation_status(jso({})))
        self.assertEqual('UNKNOWN', calculate_transportation_status(jso({'event_type': 'KKK'})))
        self.assertEqual('IN_PORT', calculate_transportation_status(jso({'event_type': 'RECEIVE'})))
        self.assertEqual('ONBOARD_CARRIER', calculate_transportation_status(jso({'event_type': 'LOAD'})))
        self.assertEqual('IN_PORT', calculate_transportation_status(jso({'event_type': 'UNLOAD'})))
        self.assertEqual('IN_PORT', calculate_transportation_status(jso({'event_type': 'CUSTOMS'})))
        self.assertEqual('CLAIMED', calculate_transportation_status(jso({'event_type': 'CLAIM'})))

if __name__ == '__main__':
    unittest.main()


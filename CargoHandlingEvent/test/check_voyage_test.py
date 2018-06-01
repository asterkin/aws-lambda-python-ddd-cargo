from check_voyage import check_voyage
from matte.jso import jso
import unittest

class TestVyageChecking(unittest.TestCase):
    def test(self):
        self.assertEqual('EVENT_TYPE_IS_MISSING', check_voyage(jso({})))
        self.assertEqual('OK', check_voyage(jso({'event_type': 'RECEIVE'})))
        self.assertEqual('UNEXPECTED_VOYAGE_REFERENCE', check_voyage(jso({'event_type': 'RECEIVE', 'voyage': 'XYZ'})))
        self.assertEqual('VOYAGE_REF_IS_MISSING', check_voyage(jso({'event_type': 'LOAD'})))
        self.assertEqual('VOYAGE_REF_IS_MISSING', check_voyage(jso({'event_type': 'UNLOAD'})))
        self.assertEqual('OK', check_voyage(jso({'event_type': 'LOAD', 'voyage': 'XYZ'})))

if __name__ == '__main__':
    unittest.main()

from checkVoyage import checkVoyage
from mattea.jso import jso
import unittest

class TestVyageChecking(unittest.TestCase):
    def test(self):
        self.assertEqual('EVENT_TYPE_IS_MISSING', checkVoyage(jso({})))
        self.assertEqual('OK', checkVoyage(jso({'eventType': 'RECEIVE'})))
        self.assertEqual('UNEXPECTED_VOYAGE_REFERENCE', checkVoyage(jso({'eventType': 'RECEIVE', 'voyage': 'XYZ'})))
        self.assertEqual('VOYAGE_REF_IS_MISSING', checkVoyage(jso({'eventType': 'LOAD'})))
        self.assertEqual('VOYAGE_REF_IS_MISSING', checkVoyage(jso({'eventType': 'UNLOAD'})))
        self.assertEqual('OK', checkVoyage(jso({'eventType': 'LOAD', 'voyage': 'XYZ'})))

if __name__ == '__main__':
    unittest.main()

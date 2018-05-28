from isCargoSpecificationSatisfied import lambda_handler
import unittest

specification = {
    'origin': 'ABC',
    'destination': 'DEF',
    'arrivalDeadline': 123456789
}

empty_itinerary = []

class TestCargoSpecificationChecking(unittest.TestCase):
    def testNone(self):
        self.assertEqual(False, lambda_handler({}, None))
        self.assertEqual(False, lambda_handler({'specification': specification}, None))
        self.assertEqual(False, lambda_handler({'specification': specification, 'itinerary': empty_itinerary}, None))

    def testGood(self):
        itinerary = [
            {'loadLocation': 'ABC'},
            {'unloadLocation': 'DEF', 'unloadTime': 123456788}
        ]
        self.assertEqual(True, lambda_handler({'specification': specification, 'itinerary': itinerary}, None))

    def testWrongOrigin(self):
        itinerary = [
            {'loadLocation': 'ABCD'},
            {'unloadLocation': 'DEF', 'unloadTime': 123456788}
        ]
        self.assertEqual(False, lambda_handler({'specification': specification, 'itinerary': itinerary}, None))

    def testWrongDestination(self):
        itinerary = [
            {'loadLocation': 'ABC'},
            {'unloadLocation': 'DDEF', 'unloadTime': 123456788}
        ]
        self.assertEqual(False, lambda_handler({'specification': specification, 'itinerary': itinerary}, None))

    def testTooLate(self):
        itinerary = [
            {'loadLocation': 'ABC'},
            {'unloadLocation': 'DEF', 'unloadTime': 123456799}
        ]
        self.assertEqual(False, lambda_handler({'specification': specification, 'itinerary': itinerary}, None))

if __name__ == '__main__':
    unittest.main()

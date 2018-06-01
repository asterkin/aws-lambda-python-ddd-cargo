from is_cargo_specification_satisfied import is_cargo_specification_satisfied
import unittest
from matte.jso import jso

specification = jso({
    'origin': 'ABC',
    'destination': 'DEF',
    'arrival_dead_line': 123456789
})

class TestCargoSpecificationChecking(unittest.TestCase):
    def test_none(self):
        self.assertFalse(is_cargo_specification_satisfied(None, None))
        self.assertFalse(is_cargo_specification_satisfied(specification, None))
        self.assertFalse(is_cargo_specification_satisfied(specification, []))

    def test_good(self):
        itinerary = jso([
            {'load': {'location': 'ABC'}},
            {'unload': {'location': 'DEF', 'time': 123456788}}
        ])
        self.assertTrue(is_cargo_specification_satisfied(specification, itinerary))

    def test_wrong_origin(self):
        itinerary = jso([
            {'load' : {'location': 'ABCD'}},
            {'unload': {'location': 'DEF', 'time': 123456788}}
        ])
        self.assertFalse(is_cargo_specification_satisfied(specification, itinerary))

    def test_wrong_destination(self):
        itinerary = jso([
            {'load' : {'location': 'ABC'}},
            {'unload' : {'location': 'DDEF', 'time': 123456788}}
        ])
        self.assertFalse(is_cargo_specification_satisfied(specification, itinerary))

    def test_too_late(self):
        itinerary = jso([
            {'load' : {'location': 'ABC'}},
            {'unload' : {'location': 'DEF', 'time': 123456799}}
        ])
        self.assertFalse(is_cargo_specification_satisfied(specification, itinerary))

if __name__ == '__main__':
    unittest.main()

from calculateDeliveryStatus import calculateDeliveryStatus
from mattea.jso import jso
import unittest

class TestDeliveryStatus(unittest.TestCase):
  def setUp(self):
    self.itinerary = [
        {
          "loadLocation": "ABC",
          "loadTime": 1526897537633,
          "unloadLocation": "DEF",
          "unloadTime": 1526897537635,
          "voyage": "XYZ"
        },
        {
          "loadLocation": "DEF",
          "loadTime": 1526897537637,
          "unloadLocation": "GHI",
          "unloadTime": 1526897537637,
          "voyage": "STU"
        }    
    ]
  def test_unknown(self):
    input = jso({
      "lastEvent": {
        "location": "ABC",
        "voyage": "XYZ",
        "eventType": "RECEIVE"
      },
      "itinerary": []
    })
    self.assertEqual('UNKNOWN', calculateDeliveryStatus(input.lastEvent, input.itinerary))

  def test_ahead_of_schedule(self):
    input = jso({
      "lastEvent": {
        "location": "ABC",
        "voyage": "XYZ",
        "eventType": "RECEIVE",
        "completionTime": 1526897537632
      },
      "itinerary": self.itinerary
    })
    self.assertEqual('AHEAD_OF_SCHEDULE', calculateDeliveryStatus(input.lastEvent, input.itinerary))

  def test_on_schedule(self):
    input = jso({
      "lastEvent": {
        "location": "ABC",
        "voyage": "XYZ",
        "eventType": "RECEIVE",
        "completionTime": 1526897537633
      },
      "itinerary": self.itinerary
    })
    self.assertEqual('ON_SCHEDULE', calculateDeliveryStatus(input.lastEvent, input.itinerary))

  def test_behind_schedule(self):
    input = jso({
      "lastEvent": {
        "location": "ABC",
        "voyage": "XYZ",
        "eventType": "RECEIVE",
        "completionTime": 1526897537635
      },
      "itinerary": self.itinerary
    })
    self.assertEqual('BEHIND_SCHEDULE', calculateDeliveryStatus(input.lastEvent, input.itinerary))

  def test_misdirected(self):
    input = jso({
      "lastEvent": {
        "location": "DEF",
        "voyage": "XYZ",
        "eventType": "RECEIVE",
        "completionTime": 1526897537635
      },
      "itinerary": self.itinerary
    })
    self.assertEqual('MISDIRECTED', calculateDeliveryStatus(input.lastEvent, input.itinerary))

  def test_load(self):
    input = jso({
      "lastEvent": {
        "location": "ABC",
        "voyage": "XYZ",
        "eventType": "LOAD",
        "completionTime": 1526897537633
      },
      "itinerary": self.itinerary
    })
    self.assertEqual('ON_SCHEDULE', calculateDeliveryStatus(input.lastEvent, input.itinerary))

  def test_unload(self):
    input = jso({
      "lastEvent": {
        "location": "DEF",
        "voyage": "XYZ",
        "eventType": "UNLOAD",
        "completionTime": 1526897537637
      },
      "itinerary": self.itinerary
    })
    self.assertEqual('BEHIND_SCHEDULE',calculateDeliveryStatus(input.lastEvent, input.itinerary))

  def test_customs(self):
    input = jso({
      "lastEvent": {
        "location": "GHI",
        "voyage": "STU",
        "eventType": "CUSTOMS",
        "completionTime": 1526897537632
      },
      "itinerary": self.itinerary
    })
    self.assertEqual('AHEAD_OF_SCHEDULE', calculateDeliveryStatus(input.lastEvent, input.itinerary))

  def test_claim(self):
    input = jso({
      "lastEvent": {
        "location": "GHI",
        "voyage": "STU",
        "eventType": "CLAIM",
        "completionTime": 1526897537632
      },
      "itinerary": self.itinerary
    })
    self.assertEqual('AHEAD_OF_SCHEDULE', calculateDeliveryStatus(input.lastEvent, input.itinerary))

if __name__ == '__main__':
    unittest.main()


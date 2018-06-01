from calculate_delivery_status import calculate_delivery_status
from matte.jso import jso
import unittest

class TestDeliveryStatus(unittest.TestCase):
  def setUp(self):
    self.itinerary = [
        {
          "load" : {
            "location": "ABC",
            "time": 1526897537633
          },
          "unload" : {
            "location": "DEF",
            "time": 1526897537635
          },
          "voyage": "XYZ"
        },
        {
          "load" : {
            "location": "DEF",
            "time": 1526897537637
          },
          "unload" : {
            "location": "GHI",
            "time": 1526897537637
          },
          "voyage": "STU"
        }    
    ]
  def test_unknown(self):
    input = jso({
      "last_event": {
        "location": "ABC",
        "voyage": "XYZ",
        "event_type": "RECEIVE"
      },
      "itinerary": []
    })
    self.assertEqual('UNKNOWN', calculate_delivery_status(input.last_event, input.itinerary))

  def test_ahead_of_schedule(self):
    input = jso({
      "last_event": {
        "location": "ABC",
        "voyage": "XYZ",
        "event_type": "RECEIVE",
        "completion_time": 1526897537632
      },
      "itinerary": self.itinerary
    })
    self.assertEqual('AHEAD_OF_SCHEDULE', calculate_delivery_status(input.last_event, input.itinerary))

  def test_on_schedule(self):
    input = jso({
      "last_event": {
        "location": "ABC",
        "voyage": "XYZ",
        "event_type": "RECEIVE",
        "completion_time": 1526897537633
      },
      "itinerary": self.itinerary
    })
    self.assertEqual('ON_SCHEDULE', calculate_delivery_status(input.last_event, input.itinerary))

  def test_behind_schedule(self):
    input = jso({
      "last_event": {
        "location": "ABC",
        "voyage": "XYZ",
        "event_type": "RECEIVE",
        "completion_time": 1526897537635
      },
      "itinerary": self.itinerary
    })
    self.assertEqual('BEHIND_SCHEDULE', calculate_delivery_status(input.last_event, input.itinerary))

  def test_misdirected(self):
    input = jso({
      "last_event": {
        "location": "DEF",
        "voyage": "XYZ",
        "event_type": "RECEIVE",
        "completion_time": 1526897537635
      },
      "itinerary": self.itinerary
    })
    self.assertEqual('MISDIRECTED', calculate_delivery_status(input.last_event, input.itinerary))

  def test_load(self):
    input = jso({
      "last_event": {
        "location": "ABC",
        "voyage": "XYZ",
        "event_type": "LOAD",
        "completion_time": 1526897537633
      },
      "itinerary": self.itinerary
    })
    self.assertEqual('ON_SCHEDULE', calculate_delivery_status(input.last_event, input.itinerary))

  def test_unload(self):
    input = jso({
      "last_event": {
        "location": "DEF",
        "voyage": "XYZ",
        "event_type": "UNLOAD",
        "completion_time": 1526897537637
      },
      "itinerary": self.itinerary
    })
    self.assertEqual('BEHIND_SCHEDULE',calculate_delivery_status(input.last_event, input.itinerary))

  def test_customs(self):
    input = jso({
      "last_event": {
        "location": "GHI",
        "voyage": "STU",
        "event_type": "CUSTOMS",
        "completion_time": 1526897537632
      },
      "itinerary": self.itinerary
    })
    self.assertEqual('AHEAD_OF_SCHEDULE', calculate_delivery_status(input.last_event, input.itinerary))

  def test_claim(self):
    input = jso({
      "last_event": {
        "location": "GHI",
        "voyage": "STU",
        "event_type": "CLAIM",
        "completion_time": 1526897537632
      },
      "itinerary": self.itinerary
    })
    self.assertEqual('AHEAD_OF_SCHEDULE', calculate_delivery_status(input.last_event, input.itinerary))

if __name__ == '__main__':
    unittest.main()


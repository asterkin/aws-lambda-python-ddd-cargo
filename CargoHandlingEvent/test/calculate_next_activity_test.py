from calculate_next_activity import calculate_next_activity
from matte.jso import jso
import unittest

class TestNextActivity(unittest.TestCase):

  def test_load(self):
    input = jso({
      "last_event": {
        "location": "ABC",
        "voyage": "XYZ",
        "event_type": "LOAD"
      },
      "itinerary": [
        {
          "load" : {
            "location": "ABC"
          },
          "unload" : {
            "location": "DEF",
            "time": 1526897537633
          },
          "voyage": "XYZ"
        }
      ]
    })
    self.assertEqual({'event_type': 'UNLOAD', 'location': 'DEF', 'voyage': 'XYZ', 'completion_time': 1526897537633}, calculate_next_activity(input.last_event, input.itinerary))

  def test_unload_claim(self):
    input = jso({
      "last_event": {
        "location": "DEF",
        "voyage": "XYZ",
        "event_type": "UNLOAD"
      },
      "itinerary": [
        {
          "load" : {
            "location": "ABC"
          },
          "unload" : {
            "location": "DEF",
            "time": 1526897537633
          },
          "voyage": "XYZ"
        }
      ]
    })
    self.assertEqual({'event_type': 'CLAIM', 'location': 'DEF'}, calculate_next_activity(input.last_event, input.itinerary))

  def test_receive(self):
    input = jso({
      "last_event": {
        "location": "DEF",
        "event_type": "RECEIVE"
      },
      "itinerary": [
        {
          "load" : {
            "location": "ABC",
            "time": 1526897537633
          },
          "voyage": "XYZ"
        }
      ]
    })
    self.assertEqual({'event_type': 'LOAD', 'location': 'ABC', 'voyage': 'XYZ', 'completion_time': 1526897537633}, calculate_next_activity(input.last_event, input.itinerary))

  def test_unload_load(self):
    input = jso({
      "last_event": {
        "location": "DEF",
        "voyage": "XYZ",
        "event_type": "UNLOAD"
      },
      "itinerary": [
        {
          "load" : {
            "location": "ABC"
          },
          "unload" : {
            "location": "DEF",
            "time": 1526897537633
          },
          "voyage": "XYZ"
        },
        {
          "load" : {
            "location": "DEF",
            "time": 1526897537633
          },
          "voyage": "STU"
        }    
      ]
    })
    self.assertEqual({'event_type': 'LOAD', 'location': 'DEF', 'voyage': 'STU', 'completion_time': 1526897537633}, calculate_next_activity(input.last_event, input.itinerary))

  def test_no_activity(self):
    input = jso({
      "last_event": {
        "location": "DEF",
        "voyage": "LMN",
        "event_type": "UNLOAD"
      },
      "itinerary": [
        {
          "load" : {
            "location": "ABC"
          },
          "unload" : {
            "location": "DEF",
            "time": 1526897537633
          },
          "voyage": "XYZ"
        },
        {
          "load" : {
            "location": "DEF",
            "time": 1526897537633
          },
          "unload" : {
            "location" : "MNO",
            "time" : 1526897537633
          },
          "voyage": "STU"
        }    
      ]
    })
    self.assertEqual({'event_type': 'NO_ACTIVITY'}, calculate_next_activity(input.last_event, input.itinerary))

  def test_customs(self):
    input = jso({
      "last_event": {
        "location": "DEF",
        "event_type": "CUSTOMS"
      },
      "itinerary": [
        {
          "load" : {
            "location": "ABC"
          },
          "unload" : {
            "location": "DEF",
            "time": 1526897537633
          },
          "voyage": "XYZ"
        },
        {
          "load" : {
            "location": "DEF",
            "time": 1526897537633
          },
          "voyage": "STU"
        }    
      ]
    })
    self.assertEqual({'event_type': 'NO_ACTIVITY'}, calculate_next_activity(input.last_event, input.itinerary))

if __name__ == '__main__':
    unittest.main()









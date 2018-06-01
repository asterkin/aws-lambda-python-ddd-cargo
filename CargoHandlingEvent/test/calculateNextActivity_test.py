from calculateNextActivity import calculateNextActivity
from mattea.jso import jso
import unittest

class TestDeliveryStatus(unittest.TestCase):

  def test_load(self):
    input = jso({
      "lastEvent": {
        "location": "ABC",
        "voyage": "XYZ",
        "eventType": "LOAD"
      },
      "itinerary": [
        {
          "loadLocation": "ABC",
          "unloadLocation": "DEF",
          "unloadTime": 1526897537633,
          "voyage": "XYZ"
        }
      ]
    })
    self.assertEqual({'eventType': 'UNLOAD', 'location': 'DEF', 'voyage': 'XYZ', 'completionTime': 1526897537633}, calculateNextActivity(input.lastEvent, input.itinerary))

  def test_unload_claim(self):
    input = jso({
      "lastEvent": {
        "location": "DEF",
        "voyage": "XYZ",
        "eventType": "UNLOAD"
      },
      "itinerary": [
        {
          "loadLocation": "ABC",
          "unloadLocation": "DEF",
          "unloadTime": 1526897537633,
          "voyage": "XYZ"
        }
      ]
    })
    self.assertEqual({'eventType': 'CLAIM', 'location': 'DEF'}, calculateNextActivity(input.lastEvent, input.itinerary))

    def test_receive(self):
      input = jso({
        "lastEvent": {
          "location": "DEF",
          "eventType": "RECEIVE"
        },
        "itinerary": [
          {
            "loadLocation": "ABC",
            "loadTime": 1526897537633,
            "voyage": "XYZ"
          }
        ]
      })
      self.assertEqual({'eventType': 'LOAD', 'location': 'ABC', 'voyage': 'XYZ', 'completionTime': 1526897537633}, calculateNextActivity(input.lastEvent, input.itinerary))

    def test_unload_load(self):
      input = jso({
        "lastEvent": {
          "location": "DEF",
          "voyage": "XYZ",
          "eventType": "UNLOAD"
        },
        "itinerary": [
          {
            "loadLocation": "ABC",
            "unloadLocation": "DEF",
            "unloadTime": 1526897537633,
            "voyage": "XYZ"
          },
          {
            "loadLocation": "DEF",
            "loadTime": 1526897537633,
            "voyage": "STU"
          }    
        ]
      })
      self.assertEqual({'eventType': 'LOAD', 'location': 'DEF', 'voyage': 'STU', 'completionTime': 1526897537633}, calculateNextActivity(input.lastEvent, input.itinerary))

  def test_no_activity(self):
    input = jso({
      "lastEvent": {
        "location": "DEF",
        "voyage": "LMN",
        "eventType": "UNLOAD"
      },
      "itinerary": [
        {
          "loadLocation": "ABC",
          "unloadLocation": "DEF",
          "unloadTime": 1526897537633,
          "voyage": "XYZ"
        },
        {
          "loadLocation": "DEF",
          "loadTime": 1526897537633,
          "voyage": "STU"
        }    
      ]
    })
    self.assertEqual({'eventType': 'NO_ACTIVITY'}, calculateNextActivity(input.lastEvent, input.itinerary))

  def test_customs(self):
    input = jso({
      "lastEvent": {
        "location": "DEF",
        "eventType": "CUSTOMS"
      },
      "itinerary": [
        {
          "loadLocation": "ABC",
          "unloadLocation": "DEF",
          "unloadTime": 1526897537633,
          "voyage": "XYZ"
        },
        {
          "loadLocation": "DEF",
          "loadTime": 1526897537633,
          "voyage": "STU"
        }    
      ]
    })
    self.assertEqual({'eventType': 'NO_ACTIVITY'}, calculateNextActivity(input.lastEvent, input.itinerary))

if __name__ == '__main__':
    unittest.main()









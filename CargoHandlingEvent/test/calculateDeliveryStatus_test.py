from calculateDeliveryStatus import lambda_handler
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
    input = {
      "lastEvent": {
        "location": "ABC",
        "voyage": "XYZ",
        "eventType": "RECEIVE"
      },
      "itinerary": []
    }
    self.assertEqual('UNKNOWN', lambda_handler(input, None))

  def test_ahead_of_schedule(self):
    input = {
      "lastEvent": {
        "location": "ABC",
        "voyage": "XYZ",
        "eventType": "RECEIVE",
        "completionTime": 1526897537632
      },
      "itinerary": self.itinerary
    }
    self.assertEqual('AHEAD_OF_SCHEDULE', lambda_handler(input, None))

  def test_on_schedule(self):
    input = {
      "lastEvent": {
        "location": "ABC",
        "voyage": "XYZ",
        "eventType": "RECEIVE",
        "completionTime": 1526897537633
      },
      "itinerary": self.itinerary
    }
    self.assertEqual('ON_SCHEDULE', lambda_handler(input, None))

  def test_behind_schedule(self):
    input = {
      "lastEvent": {
        "location": "ABC",
        "voyage": "XYZ",
        "eventType": "RECEIVE",
        "completionTime": 1526897537635
      },
      "itinerary": self.itinerary
    }
    self.assertEqual('BEHIND_SCHEDULE', lambda_handler(input, None))

  def test_misdirected(self):
    input = {
      "lastEvent": {
        "location": "DEF",
        "voyage": "XYZ",
        "eventType": "RECEIVE",
        "completionTime": 1526897537635
      },
      "itinerary": self.itinerary
    }
    self.assertEqual('MISDIRECTED', lambda_handler(input, None))

  def test_load(self):
    input = {
      "lastEvent": {
        "location": "ABC",
        "voyage": "XYZ",
        "eventType": "LOAD",
        "completionTime": 1526897537633
      },
      "itinerary": self.itinerary
    }
    self.assertEqual('ON_SCHEDULE', lambda_handler(input, None))

  def test_unload(self):
    input = {
      "lastEvent": {
        "location": "DEF",
        "voyage": "XYZ",
        "eventType": "UNLOAD",
        "completionTime": 1526897537637
      },
      "itinerary": self.itinerary
    }
    self.assertEqual('BEHIND_SCHEDULE',lambda_handler(input, None))

  def test_customs(self):
    input = {
      "lastEvent": {
        "location": "GHI",
        "voyage": "STU",
        "eventType": "CUSTOMS",
        "completionTime": 1526897537632
      },
      "itinerary": self.itinerary
    }
    self.assertEqual('AHEAD_OF_SCHEDULE', lambda_handler(input, None))

  def test_claim(self):
    input = {
      "lastEvent": {
        "location": "GHI",
        "voyage": "STU",
        "eventType": "CLAIM",
        "completionTime": 1526897537632
      },
      "itinerary": self.itinerary
    }
    self.assertEqual('AHEAD_OF_SCHEDULE', lambda_handler(input, None))

if __name__ == '__main__':
    unittest.main()


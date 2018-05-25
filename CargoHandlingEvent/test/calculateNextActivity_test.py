from calculateNextActivity import lambda_handler
import unittest

class TestDeliveryStatus(unittest.TestCase):

  def test_load(self):
    input = {
      "lastEvent": {
        "location": "ABC",
        "voyageId": "XYZ",
        "eventType": "LOAD"
      },
      "itinerary": [
        {
          "loadLocation": "ABC",
          "unloadLocation": "DEF",
          "unloadTime": 1526897537633,
          "voyageId": "XYZ"
        }
      ]
    }
    self.assertEqual({'eventType': 'UNLOAD', 'location': 'DEF', 'voyageId': 'XYZ', 'completionTime': 1526897537633}, lambda_handler(input, None))

  def test_unload_claim(self):
    input = {
      "lastEvent": {
        "location": "DEF",
        "voyageId": "XYZ",
        "eventType": "UNLOAD"
      },
      "itinerary": [
        {
          "loadLocation": "ABC",
          "unloadLocation": "DEF",
          "unloadTime": 1526897537633,
          "voyageId": "XYZ"
        }
      ]
    }
    self.assertEqual({'eventType': 'CLAIM', 'location': 'DEF'}, lambda_handler(input, None))

    def test_receive(self):
      input = {
        "lastEvent": {
          "location": "DEF",
          "eventType": "RECEIVE"
        },
        "itinerary": [
          {
            "loadLocation": "ABC",
            "loadTime": 1526897537633,
            "voyageId": "XYZ"
          }
        ]
      }
      self.assertEqual({'eventType': 'LOAD', 'location': 'ABC', 'voyageId': 'XYZ', 'completionTime': 1526897537633}, lambda_handler(input, None))

    def test_unload_load(self):
      input = {
        "lastEvent": {
          "location": "DEF",
          "voyageId": "XYZ",
          "eventType": "UNLOAD"
        },
        "itinerary": [
          {
            "loadLocation": "ABC",
            "unloadLocation": "DEF",
            "unloadTime": 1526897537633,
            "voyageId": "XYZ"
          },
          {
            "loadLocation": "DEF",
            "loadTime": 1526897537633,
            "voyageId": "STU"
          }    
        ]
      }
      self.assertEqual({'eventType': 'LOAD', 'location': 'DEF', 'voyageId': 'STU', 'completionTime': 1526897537633}, lambda_handler(input, None))

  def test_no_activity(self):
    input = {
      "lastEvent": {
        "location": "DEF",
        "voyageId": "LMN",
        "eventType": "UNLOAD"
      },
      "itinerary": [
        {
          "loadLocation": "ABC",
          "unloadLocation": "DEF",
          "unloadTime": 1526897537633,
          "voyageId": "XYZ"
        },
        {
          "loadLocation": "DEF",
          "loadTime": 1526897537633,
          "voyageId": "STU"
        }    
      ]
    }
    self.assertEqual({'eventType': 'NO_ACTIVITY'}, lambda_handler(input, None))

  def test_customs(self):
    input = {
      "lastEvent": {
        "location": "DEF",
        "eventType": "CUSTOMS"
      },
      "itinerary": [
        {
          "loadLocation": "ABC",
          "unloadLocation": "DEF",
          "unloadTime": 1526897537633,
          "voyageId": "XYZ"
        },
        {
          "loadLocation": "DEF",
          "loadTime": 1526897537633,
          "voyageId": "STU"
        }    
      ]
    }
    self.assertEqual({'eventType': 'NO_ACTIVITY'}, lambda_handler(input, None))

if __name__ == '__main__':
    unittest.main()









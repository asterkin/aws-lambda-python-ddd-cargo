"""Store Cargo Itinerary."""

from Cargo import Itineraries

itineraries = Itineraries.put_client()

def put_itinerary(cargo, schedule):
    item = { #security measure not to flush arbitrary object into DB
        'cargo': cargo,
        'schedule': schedule #TODO: shall I check every array element
    }
    return itineraries.put_item(item, False) #TODO: error handling, write capacity

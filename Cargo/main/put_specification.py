"""Store Cargo specification."""

from Cargo import Specifications
from matte import PutClient

itineraries = PutClient(Specifications)

def put_itinerary(cargo, schedule):
    item = { #security measure not to flush arbitrary object into DB
        'cargo': cargo,
        'schedule': schedule #TODO: shall I check every array element
    }
    return itineraries.put_item(item, False) #TODO: error handling, write capacity

def put_specification(cargo, specification):
    item = { #security measure not to flush arbitrary object into DB
        'cargo': cargo,
        'origin': specification.origin,
        'destination': specification.destination,
        'arrival_dead_line': specification.arrival_dead_line
    }
    return specifications.put_item(item, False) #TODO: error handling, write capacity

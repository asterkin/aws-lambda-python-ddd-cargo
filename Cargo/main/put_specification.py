"""Store Cargo specification."""

from Cargo import Specifications

specifications = Specifications.put_client()

def put_specification(cargo, specification):
    item = { #security measure not to flush arbitrary object into DB
        'cargo': cargo,
        'origin': specification.origin,
        'destination': specification.destination,
        'arrival_dead_line': specification.arrival_dead_line
    }
    return specifications.put_item(item, False) #TODO: error handling, write capacity

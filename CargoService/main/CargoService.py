"""Encapsulates Cargo Repository and all relevant computations."""
from nahash import dropNone
from Repository import Repository

CARGO = 'cargo'

def resources():
    return [
        Repository('Cargo', hashKey = {'name': CARGO, 'type': 'S'}),
        Repository('Specification', hashKey = {'name': CARGO, 'type': 'S'}),
        Repository('Itinerary', hashKey = {'name': CARGO, 'type': 'S'}),        
    ]


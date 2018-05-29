"""Encapsulates Voyage and Location Repositories and all relevant computations."""
from nahash import dropNone
from Repository import Repository

def resources():
    return [
        Repository('Voyage', hashKey = {'name': 'voyage', 'type': 'S'}),
        Repository('Location', hashKey = {'name': 'location', 'type': 'S'}),
    ]

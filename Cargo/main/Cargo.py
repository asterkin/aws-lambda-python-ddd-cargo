"""Encapsulates Cargo Repository and all relevant computations."""
from matte import Repository

CARGO = 'cargo'
CARGO_KEY = {CARGO : str}

#TODO: automatically infer repository name
Cargoes = Repository('Cargo', hashKey = CARGO_KEY)
Specifications = Repository('Specification', hashKey = CARGO_KEY)
Itineraries = Repository('Itinerary', hashKey = CARGO_KEY)


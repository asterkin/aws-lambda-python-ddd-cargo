"""Encapsulates Cargo Repository and all relevant computations."""
import matte

CARGO = 'cargo'
CARGO_KEY = {CARGO : str}

Cargoes = matte.repository('Cargoes', hashKey = CARGO_KEY)
Specifications = matte.repository('Specifications', hashKey = CARGO_KEY)
Itineraries = matte.repository('Itineraries', hashKey = CARGO_KEY)


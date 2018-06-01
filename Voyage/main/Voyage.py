"""Encapsulates Voyage and Location Repositories and all relevant computations."""
from matte import Repository

Voyages = Repository('Voyage', hashKey = {'voyage' : str})
Locations = Repository('Location', hashKey = {'location' : str})


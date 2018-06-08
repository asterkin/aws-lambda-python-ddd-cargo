"""Encapsulates Voyage and Location Repositories and all relevant computations."""
import matte

Voyages = matte.repository('Voyage', hashKey = {'voyage' : str})
Locations = matte.repository('Location', hashKey = {'location' : str})


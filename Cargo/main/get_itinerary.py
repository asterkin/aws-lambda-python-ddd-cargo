"""Retrieve Cargo itinerary for the given id."""

from Cargo import Itineraries
from matte import GetClient

itineraries = GetClient(Itineraries)

def get_itinerary(cargo):
    return itineraries.get_item(cargo)


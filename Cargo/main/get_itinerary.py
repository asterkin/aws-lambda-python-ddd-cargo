"""Retrieve Cargo itinerary for the given id."""

from Cargo import Itineraries

itineraries = Itineraries.get_client()

def get_itinerary(cargo):
    return itineraries.get_item(cargo)


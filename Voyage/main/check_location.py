""" Check whether location referece is correct."""

from Voyage import Locations

locations = Locations.get_client()

def check_location(location):
    return locations.has_item(location)


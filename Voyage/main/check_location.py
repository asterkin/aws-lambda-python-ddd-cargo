""" Check whether location referece is correct."""

from Voyage import Locations
from matte import GetClient

locations = GetClient(Locations)

def check_location(location):
    return locations.has_item(location)


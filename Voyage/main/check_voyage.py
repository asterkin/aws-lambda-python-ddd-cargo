""" Check whether voyage referece is correct."""

from Voyage import Voyages
from matte import GetClient

voyages = GetClient(Voyages)

def check_voyage(voyage):
    return voyages.has_item(voyage)

""" Check whether voyage referece is correct."""

from Voyage import Voyages

voyages = Voyages.get_client()

def check_voyage(voyage):
    return voyages.has_item(voyage)

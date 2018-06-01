"""Retrieve Cargo specification for the given id."""

from Cargo import Specifications
from matte import GetClient

specifications = GetClient(Specifications)

def get_specification(cargo):
    return specifications.get_item(cargo)

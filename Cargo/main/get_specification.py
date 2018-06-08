"""Retrieve Cargo specification for the given id."""

from Cargo import Specifications

specifications = Specifications.get_client()

def get_specification(cargo):
    return specifications.get_item(cargo)

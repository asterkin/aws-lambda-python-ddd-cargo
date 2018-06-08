""" Check whether cargo reference is correct."""

from Cargo import Cargoes

cargoes = Cargoes.get_client()

def check_cargo(cargo):
    return cargoes.has_item(cargo)

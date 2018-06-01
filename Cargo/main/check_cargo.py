""" Check whether cargo reference is correct."""

from matte import GetClient
from Cargo import Cargoes

cargoes = GetClient(Cargoes)

def check_cargo(cargo):
    return cargoes.has_item(cargo)

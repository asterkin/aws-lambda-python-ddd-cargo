""" Check whether cargo referece is correct."""

from matte import GetClient
from Cargo import Cargoes

cargoes = GetClient(Cargoes)

def check_cargo(cargo):
    if not cargo: return 'CARGO_REFERENCE_IS_MISSING'
    return 'OK' if cargoes.has_item(cargo) else 'CARGO_NOT_FOUND'

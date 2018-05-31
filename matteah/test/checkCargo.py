from matteah import Repository, GetClient

Cargoes = Repository(name='Cargo', hashKey='cargo')

cargoes = GetClient(Cargoes)

def checkCargo(cargo: str) -> str:
    return cargo

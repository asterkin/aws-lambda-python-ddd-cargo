from mattea import Repository, GetClient

Cargoes = Repository('Cargo', hashKey={'cargo' : str})

cargoes = GetClient(Cargoes)

def checkCargo(cargo: str) -> str:
    return cargo

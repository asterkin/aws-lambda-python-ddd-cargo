from matte import Repository, GetClient

Cargoes = Repository('Cargo', hashKey={'cargo' : str})

cargoes = GetClient(Cargoes)

def check_cargo(cargo: str) -> str:
    return cargo

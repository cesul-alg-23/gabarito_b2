def calcular_qtde_carne(pessoas: int, sexo: str) -> int:
    if sexo == 'M':
        return pessoas * 400
    else:
        return pessoas * 300


def calcular_qtde_cerveja(pessoas: int, sexo: str) -> int:
    if sexo == 'M':
        return pessoas * 5
    else:
        return pessoas * 2

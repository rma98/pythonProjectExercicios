def metade(p):
    metade = p / 2
    return metade


def dobro(p):
    dobro = p * 2
    return dobro


def aumentar(p, porcento=0):
    novoPreco = p + (p * porcento/100)
    return novoPreco


def diminuir(p, porcento=0):
    novoPreco = p - (p * porcento/100)
    return novoPreco

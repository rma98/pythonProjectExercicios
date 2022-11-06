def metade(p=0):
    metade = p / 2
    return metade


def dobro(p=0):
    dobro = p * 2
    return dobro


def aumentar(p=0, porcento=0):
    novoPreco = p + (p * porcento/100)
    return novoPreco


def diminuir(p, porcento=0):
    novoPreco = p - (p * porcento/100)
    return novoPreco


def moeda(p=0, moeda ='R$'):
    return f'{moeda}{p:>.2f}'.replace('.', ',')

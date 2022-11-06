def metade(p=0, formatado=False):
    metade = p / 2
    return metade if not formatado else moeda(p)


def dobro(p=0, formatado=False):
    dobro = p * 2
    return dobro if not formatado else moeda(p)


def aumentar(p=0, porcento=0, formatado=False):
    novoPreco = p + (p * porcento/100)
    return novoPreco if formatado is False else moeda(p)


def diminuir(p, porcento=0, formatado=False):
    novoPreco = p - (p * porcento/100)
    return novoPreco if not formatado else moeda(p)


def moeda(p=0, moeda ='R$', formatado=False):
    return f'{moeda}{p:>.2f}'.replace('.', ',')

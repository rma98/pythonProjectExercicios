def metade(p=0, formatado=False):
    metade = p / 2
    return metade if not formatado else moeda(metade)


def dobro(p=0, formatado=False):
    dobro = p * 2
    return dobro if not formatado else moeda(dobro)


def aumentar(p=0, porcento=0, formatado=False):
    '''
    -> Calcula o aumento de um determinado preço, retornando o resultado com ou sem formatação.
    :param p: o preço que se quer reajustar
    :param porcento: qual é a porcentangem do aumento.
    :param formatado: quer a saída foramtada ou não?
    :return: o valor reajustado, com ou sem formatação.
    '''
    novoPreco = p + (p * porcento/100)
    return novoPreco if formatado is False else moeda(novoPreco)


def diminuir(p, porcento=0, formatado=False):
    novoPreco = p - (p * porcento/100)
    return novoPreco if not formatado else moeda(novoPreco)


def moeda(p=0, moeda ='R$', formatado=False):
    return f'{moeda}{p:>.2f}'.replace('.', ',')


def resumo(p=0, aumento=10, reducao=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(p, aumento, True)}')
    print(f'{reducao}% de redução: \t{diminuir(p, reducao, True)}')
    print('-' * 30)

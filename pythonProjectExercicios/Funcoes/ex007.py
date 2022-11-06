#7. Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a
# calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o
# processo de cálculo do fatorial.

def fatorial(numero, show=False):
    '''
    -> Calcula o fatorial de um número
    :param numero: o número a ser calculado.
    :param show: mostrar ou não a conta.
    :return: retorna o fatorial de um número.
    '''
    f = 1
    for c in range(numero, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' X ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, show=False))
help(fatorial)
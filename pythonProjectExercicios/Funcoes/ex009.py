#9. Crie um programa que tenha a função leiaInt(), que vai funcionar da forma semelhante à função input() do Python, só
# que fazendo a vadilação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n')

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = input(msg)
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n} ')

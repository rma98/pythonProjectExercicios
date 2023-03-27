# Faça um programa que leia algo pelo usuário e mostre na tela seu tipo primitivo e todas as informações possíveis sobre ela.

infor = input('Digite algo: ')
print(f'Tipo primitivo: {type(infor)}\nSó tem espaços? {infor.isspace()}\nÉ um número? {infor.isnumeric()}'
      f'\nÉ alfabético? {infor.isalpha()}\nÉ alfanumérico? {infor.isalnum()}\nEstá em maiúsculos? {infor.isupper()}'
      f'\nEstá em minúsculos? {infor.islower()}\nEstá capitalizada? {infor.istitle()}')

# Outras formas de fazer

# 1
infor = input('Digite algo: ')

if type(infor) == str:
    print("A entrada é uma string")
if infor.isalpha():
    print("A entrada é composta apenas de letras")
if infor.isnumeric():
    print("A entrada é composta apenas de números")
if infor.isalnum():
    print("A entrada é composta de letras e/ou números")
if infor.islower():
    print("A entrada está em minúsculas")
if infor.isupper():
    print("A entrada está em maiúsculas")
if infor.istitle():
    print("A entrada está capitalizada")
if infor.isspace():
    print("A entrada é composta apenas de espaços em branco")

# 2
infor = input('Digite algo: ')

checks = [
    ("Tipo primitivo", type(infor)),
    ("Só tem espaços?", infor.isspace()),
    ("É um número?", infor.isnumeric()),
    ("É alfabético?", infor.isalpha()),
    ("É alfanumérico?", infor.isalnum()),
    ("Está em maiúsculas?", infor.isupper()),
    ("Está em minúsculas?", infor.islower()),
    ("Está capitalizada?", infor.istitle())
]

for check in checks:
    print(f"{check[0]}: {check[1]}")

# 3
def analisar_entrada(texto):
    return {
        "Tipo primitivo": type(texto),
        "Só tem espaços?": texto.isspace(),
        "É um número?": texto.isnumeric(),
        "É alfabético?": texto.isalpha(),
        "É alfanumérico?": texto.isalnum(),
        "Está em maiúsculas?": texto.isupper(),
        "Está em minúsculas?": texto.islower(),
        "Está capitalizada?": texto.istitle()
    }

infor = input('Digite algo: ')
resultado = analisar_entrada(infor)

for key, value in resultado.items():
    print(f"{key}: {value}")

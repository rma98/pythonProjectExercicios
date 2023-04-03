# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2) / 2
print(f'Média: {media:.1f}')

# outras formas de fazer

# 1
notas = []
for i in range(2):
    notas.append(float(input(f'Nota {i+1}: ')))
media = sum(notas) / len(notas)
print(f'Média: {media:.1f}')

# 2
def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = calcular_media(nota1, nota2)
print(f'Média: {media:.1f}')

# 3
def calcular_media(*notas):
    return sum(notas) / len(notas)

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = calcular_media(nota1, nota2)
print(f'Média: {media:.1f}')

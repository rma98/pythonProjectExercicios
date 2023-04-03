# Calcule a média aritmética das três notas de um aluno e mostre, além do valor da média, uma mensagem de "Aprovado,"
# caso a média seja igual ou superior a 7; "em prova final" caso a média seja menor que 7 e maior ou igual a 4 e
# "Reprovado", caso contrário.

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
media = (nota1 + nota2 + nota3) / 3
if media >= 7:
    print("Aprovado.")
elif media < 7 and media >=4:
    print("Em prova final.")
else:
    print("Reprovado.")

# Outras formas de fazer

# 1
notas = []
for i in range(3):
    nota = float(input(f"Nota {i+1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

if media >= 7:
    print("Aprovado.")
elif 4 <= media < 7:
    print("Em prova final.")
else:
    print("Reprovado.")

# 2
nota1, nota2, nota3 = [float(input(f"Nota {i+1}: ")) for i in range(3)]
media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("Aprovado.")
elif 4 <= media < 7:
    print("Em prova final.")
else:
    print("Reprovado.")

# 3
notas = []
i = 1
while i <= 3:
    nota = float(input(f"Nota {i}: "))
    notas.append(nota)
    i += 1

media = sum(notas) / len(notas)

if media >= 7:
    print("Aprovado.")
elif 4 <= media < 7:
    print("Em prova final.")
else:
    print("Reprovado.")

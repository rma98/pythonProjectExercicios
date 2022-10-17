#4. Calcule a média aritmética das três notas de um aluno e mostre, além do valor da média, uma mensagem de "Aprovado",
# caso a média seja igual ou superior a 7; a mensagem "em prova final" caso a média seja menor que 7 e maior ou igual a
# 4; e "reprovado", caso contrário.

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
media = (n1 + n2 + n3) / 3
if media >= 7:
    print(f"Média: {media:.1f}\nAprovado!")
elif media < 7 and media >= 4:
    print(f"Média: {media:.1f}\nEm prova final!")
else:
    print(f"Média: {media:.1f}\nReprovado!")

#4. Calcule a média aritmética das três notas de um aluno e mostre, além do valor da média, uma mensagem de "Aprovado",
# caso a média seja igual ou superior a 7; a mensagem "em prova final" caso a média seja menor que 7 e maior ou igual a
# 4; e "reprovado", caso contrário.

n1 = float(input("\033[34mNota 1: \033[m"))
n2 = float(input("\033[35mNota 2: \033[m"))
n3 = float(input("\033[36mNota 3: \033[m"))
media = (n1 + n2 + n3) / 3
if media >= 7:
    print(f"\033[32mMédia: {media:.1f}\nAprovado!\033[m")
elif media < 7 and media >= 4:
    print(f"\033[33mMédia: {media:.1f}\nEm prova final!\033[m")
else:
    print(f"\033[31mMédia: {media:.1f}\nReprovado!\033[m")

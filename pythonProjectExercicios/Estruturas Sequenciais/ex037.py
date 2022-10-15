#37. Um usuário deseja um algoritmo pelo qual possa escolher que tipo de média deseja calcular a partir de três notas.
# Faça um algoritmo que leia as notas, a opção escolhida pelo usuário (1- aritmética ou 2- ponderada (3, 3, 4)) e
# calcule a média; se a opção tiver sido pela média aritmética, o usuário estará aprovado com média 6; se escolhe a
# ponderada, só estará aprovado com média 7. Informe ao usuário qual a forma de cálculo que ele escolheu, a média dele e
# se ele está aprovado ou não.

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
media_Aritmetica = (nota1 + nota2 + nota3) / 3
p1 = 3
p2 = 3
p3 = 4
media_Ponderada = (nota1 * p1 + nota2 * p2 + nota3 * p3) / (p1 + p2 + p3)

opcao = int(input("1 - Média Aritmética\n2 - Média Ponderada\n:"))
if opcao == 1:
    if media_Aritmetica >= 6:
        print(f"Média: {media_Aritmetica:.1f}\nAprovado!")
    else:
        print(f"Média: {media_Aritmetica:.2f}\nReprovado!")
elif opcao == 2:
    if media_Ponderada >= 7:
        print(f"Média: {media_Ponderada:.1f}\nAprovado!")
    else:
        print(f"Média: {media_Ponderada:.1f}\nReprovado!")
else:
    print("Opção Inválida!")

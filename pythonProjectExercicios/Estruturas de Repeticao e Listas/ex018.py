#18. Crie um programa que leia vários números inteiros pelo teclado o programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles
# (dessconsiderando o flag).

n = soma = cont = 0
while n != 999:
    numero = int(input('Digite um número [999 para parar]: '))
    if numero == 999:
        break
    soma += numero
    cont += 1
print(f'O total de números digitados foi {cont} e a soma é {soma}.')

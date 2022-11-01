#4. Desenvolva um programa que leia quatro valores e guarde-os em uma tupla. No final, mostre:
# a -> Quantas vezes apareceu o valor 9.
# b -> Em que posição foi digitado o primeiro valor 3.
# c -> Quais foram os números pares.

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segiundo valor: '))
n3 = int(input('Terceiro valor: '))
n4 = int(input('Quarto valor: '))
tupla = (n1, n2, n3, n4)
print(f'Os valores digitados foram {tupla}'
      f'\nO valor 9 apareceu {tupla.count(9)} vezes', end="")
if 3 in tupla:
    print(f'\nO valor 3 apareceu na {tupla.index(3) + 1}º posição', end="")
else:
    print('\nO valor 3 não foi digitado em nenhuma posição', end="")
print(f'\nOs valores pares digitados foram ', end="")
for n in tupla:
    if n % 2 == 0:
        print(f'{n} ', end=" ")

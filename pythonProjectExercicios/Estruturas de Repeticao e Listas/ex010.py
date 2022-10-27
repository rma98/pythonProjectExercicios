#10. Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# -> A média de idade do grupo.
# -> Qual é o nome do homem mais velho.
# -> Quantas mulheres têm menos de 20 anos.

soma_idade = 0
maior_idade_homem = 0
nome_velho = ''
total_mulher_20 = 0
for p in range(1, 5):
    print(f'{"----"} {p}º PESSOA ----')
    nome = input(f'Nome: ').strip()
    idade = int(input(f'Idade: '))
    sexo = input(f'\"M\" OU \"F\": ').strip()
    soma_idade += idade
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulher_20 += 1
print(f'A média de idade do grupo é {soma_idade / 4:.2f} anos'
      f'\nO homem mais velho tem {maior_idade_homem} anos e se chama {nome_velho}'
      f'\nAo todo são {total_mulher_20} mulheres com menos de 20 anos')

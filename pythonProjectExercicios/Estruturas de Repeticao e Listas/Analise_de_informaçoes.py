# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
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

# Outras formas de fazer

pessoas = []
total_mulher_20 = 0
for p in range(1, 5):
    print(f'{"----"} {p}º PESSOA ----')
    pessoa = {}
    pessoa['nome'] = input('Nome: ').strip()
    pessoa['idade'] = int(input('Idade: '))
    pessoa['sexo'] = input('\"M\" OU \"F\": ').strip()
    pessoas.append(pessoa)
    if pessoa['sexo'] in 'Ff' and pessoa['idade'] < 20:
        total_mulher_20 += 1
soma_idade = sum(pessoa['idade'] for pessoa in pessoas)
media_idade = soma_idade / len(pessoas)
homem_mais_velho = max((pessoa for pessoa in pessoas if pessoa['sexo'] in 'Mm'), key=lambda x: x['idade'])
mulheres_com_menos_de_20 = [pessoa for pessoa in pessoas if pessoa['sexo'] in 'Ff' and pessoa['idade'] < 20]
print(f'A média de idade do grupo é {media_idade:.2f} anos')
print(f'O homem mais velho tem {homem_mais_velho["idade"]} anos e se chama {homem_mais_velho["nome"]}')
print(f'Ao todo são {total_mulher_20} mulheres com menos de 20 anos')

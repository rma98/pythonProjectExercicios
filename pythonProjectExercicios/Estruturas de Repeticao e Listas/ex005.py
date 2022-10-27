#5. Desenvolva um programa que leia o primeiro termo e razão de uma PA. No final, mostre os 10 primeiros termos dessa
# progressão.

print(f'{"=" *32}\n10 PRIMEIROS TERMOS DE UMA PA\n{"=" *32}')
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro_termo + (10 - 1) * razao
for c in range(primeiro_termo, decimo + razao, razao):
    print(f'{c}', end=" -> ")
print('FIM')

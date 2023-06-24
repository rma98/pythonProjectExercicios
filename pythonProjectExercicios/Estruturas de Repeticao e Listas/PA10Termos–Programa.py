# Desenvolva um programa que leia o primeiro termo e razão de uma PA. No final, mostre os 10 primeiros termos dessa
# progressão.
# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> -> 5 -> 8

print(f'{"=" *32}\n10 PRIMEIROS TERMOS DE UMA PA\n{"=" *32}')
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro_termo + (10 - 1) * razao
for c in range(primeiro_termo, decimo + razao, razao):
    print(f'{c}', end=" -> ")
print('FIM')

# Outras formas de fazer

# 1
print(f'{"=" * 32}\n10 PRIMEIROS TERMOS DE UMA PA\n{"=" * 32}')
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termos = [primeiro_termo + (n - 1) * razao for n in range(1, 11)]
for termo in termos:
    print(termo, end=' -> ')
print('FIM')

# 2
print(f'{"=" * 32}\n10 PRIMEIROS TERMOS DE UMA PA\n{"=" * 32}')
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
contador = 0
termo_atual = primeiro_termo
while contador < 10:
    print(termo_atual, end=' -> ')
    termo_atual += razao
    contador += 1
print('FIM')

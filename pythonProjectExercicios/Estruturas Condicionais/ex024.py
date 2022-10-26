#24. Desenvolva um programa que leia o comprimento de três rotas e diga ao usuário se elas podem ou não formar um triângulo.

print('-=-'*20)
print('ANALISADOR DE TRIÂNGULO')
print('-=-'*20)

reta_a = int(input('Primeira reta: '))
reta_b = int(input('Segunda reta: '))
reta_c = int(input('Terceira reta: '))

if reta_a < reta_b + reta_c and reta_b < reta_a + reta_c and reta_c < reta_a + reta_b:
    print('Podem formar um triângulo!')
else:
    print('Não podem formar triângulo!')

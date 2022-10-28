#17. Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
# os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
# continuar a digitar valores.

cont = soma = maior = menor = 0
res = 'S'
while res == 'S':
    n = int(input('Número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    res = input('Deseja continuar? Digite "\S\" para continuar: ').upper()
print(f'A média dos {cont} números digitados foi {soma / cont}'
      f'\nO maior valor foi {maior} e o menor foi {menor}')

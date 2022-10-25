#39. Faça um programa que recebe três números, calcule e mostre a multiplicação desses números.

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Terceiro número: "))
print(f"{n1} x {n2} x {n3} = {n1 * n2 * n3}")

#39.1 Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input('Número: '))
print(f'Dobro: {numero *2}\nTriplo: {numero *3}\nRaiz quadrada: {numero ** (1/2):.2f}\n'
      f'Outra maneira de se calcular a raiz qaudrada usando a função pow(): {pow(numero, (1/2)):.2f}')

# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input('Número: '))
print(f'Dobro: {numero *2}\nTriplo: {numero *3}\nRaiz quadrada: {numero ** (1/2):.2f}\n'
      f'Outra maneira de se calcular a raiz qaudrada usando a função pow(): {pow(numero, (1/2)):.2f}')

# Outras formas de fazer

# 1
numero = int(input('Número: '))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** 0.5
print(f'Dobro: {dobro}\nTriplo: {triplo}\nRaiz quadrada: {raiz_quadrada:.2f}')

# 2
import math

numero = int(input('Número: '))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = math.sqrt(numero)
print(f'Dobro: {dobro}\nTriplo: {triplo}\nRaiz quadrada: {raiz_quadrada:.2f}')

# 3
numero = int(input('Número: '))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** 0.5
raiz_quadrada_formatted = f'{raiz_quadrada:.2f}' if raiz_quadrada % 1 != 0 else int(raiz_quadrada)
print(f'Dobro: {dobro}\nTriplo: {triplo}\nRaiz quadrada: {raiz_quadrada_formatted}')

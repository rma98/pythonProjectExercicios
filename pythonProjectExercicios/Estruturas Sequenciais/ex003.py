#3. Desenvolva um programa que leia uma medida em pés e  apresente o seu valor convertido em metros, lembrando que um pé
# é igual a 30,48 cetímetros.

medida_pes = float(input("Médida em pés: "))
print(f"Conversãoo: {medida_pes * 30.48}")

#3.1 Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

valor_em_metros = float(input('Valor em metros: '))
print(f'{valor_em_metros}m convertido em centímetros: {valor_em_metros * 100:.0f}cm'
      f'\n{valor_em_metros}m convertido em milímetros: {valor_em_metros * 1000:.0f}mm'
      f'\n{valor_em_metros}m convertido em quilômetros: {valor_em_metros / 1000}km'
      f'\n{valor_em_metros}m convertido em hectômetros: {valor_em_metros / 100}hm'
      f'\n{valor_em_metros}m convertido em decâmetros: {valor_em_metros / 10}dam'
      f'\n{valor_em_metros}m convertido em decímetros: {valor_em_metros * 10}dm')

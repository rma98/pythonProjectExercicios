# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

valor_em_metros = float(input('Valor em metros: '))
print(f'{valor_em_metros}m convertido em centímetros: {valor_em_metros * 100:.0f}cm'
      f'\n{valor_em_metros}m convertido em milímetros: {valor_em_metros * 1000:.0f}mm'
      f'\n{valor_em_metros}m convertido em quilômetros: {valor_em_metros / 1000}km'
      f'\n{valor_em_metros}m convertido em hectômetros: {valor_em_metros / 100}hm'
      f'\n{valor_em_metros}m convertido em decâmetros: {valor_em_metros / 10}dam'
      f'\n{valor_em_metros}m convertido em decímetros: {valor_em_metros * 10}dm')

# Outras formas de fazer

# 1
# constantes de conversão
CM_EM_METROS = 100
MM_EM_METROS = 1000
KM_EM_METROS = 0.001
HM_EM_METROS = 0.01
DAM_EM_METROS = 0.1
DM_EM_METROS = 10

# entrada de dados
valor_em_metros = float(input('Valor em metros: '))

# conversões
valor_em_centimetros = valor_em_metros * CM_EM_METROS
valor_em_milimetros = valor_em_metros * MM_EM_METROS
valor_em_quilometros = valor_em_metros * KM_EM_METROS
valor_em_hectometros = valor_em_metros * HM_EM_METROS
valor_em_decametros = valor_em_metros * DAM_EM_METROS
valor_em_decimetros = valor_em_metros * DM_EM_METROS

# saída de dados
print(f'{valor_em_metros}m convertido em centímetros: {valor_em_centimetros:.0f}cm')
print(f'{valor_em_metros}m convertido em milímetros: {valor_em_milimetros:.0f}mm')
print(f'{valor_em_metros}m convertido em quilômetros: {valor_em_quilometros:.3f}km')
print(f'{valor_em_metros}m convertido em hectômetros: {valor_em_hectometros:.2f}hm')
print(f'{valor_em_metros}m convertido em decâmetros: {valor_em_decametros:.1f}dam')
print(f'{valor_em_metros}m convertido em decímetros: {valor_em_decimetros:.0f}dm')

# 2
def metros_para_centimetros(metros):
    return metros * 100

def metros_para_milimetros(metros):
    return metros * 1000

def metros_para_quilometros(metros):
    return metros / 1000

def metros_para_hectometros(metros):
    return metros / 100

def metros_para_decametros(metros):
    return metros / 10

def metros_para_decimetros(metros):
    return metros * 10

valor_em_metros = float(input('Valor em metros: '))

print(f'{valor_em_metros}m convertido em centímetros: {metros_para_centimetros(valor_em_metros):.0f}cm')
print(f'{valor_em_metros}m convertido em milímetros: {metros_para_milimetros(valor_em_metros):.0f}mm')
print(f'{valor_em_metros}m convertido em quilômetros: {metros_para_quilometros(valor_em_metros)}km')
print(f'{valor_em_metros}m convertido em hectômetros: {metros_para_hectometros(valor_em_metros)}hm')
print(f'{valor_em_metros}m convertido em decâmetros: {metros_para_decametros(valor_em_metros)}dam')
print(f'{valor_em_metros}m convertido em decímetros: {metros_para_decimetros(valor_em_metros)}dm')

# 3
unidades = {'centímetros': 100, 'milímetros': 1000, 'quilômetros': 0.001, 'hectômetros': 0.01, 'decâmetros': 0.1, 'decímetros': 10}

valor_em_metros = float(input('Valor em metros: '))

for unidade, fator in unidades.items():
    valor_convertido = valor_em_metros * fator
    print(f'{valor_em_metros}m convertido em {unidade}: {valor_convertido:.0f}{unidade[:2]}')

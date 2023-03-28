# Desenvolva um programa que leia uma medida em pés e apresente o seu valor convertido em metros, lembrando que um pé
# é igual a 30,48 centímetros.

medida_pes = float(input("Médida em pés: "))
print(f"Conversãoo: {medida_pes * 30.48}")

# Outras formas de fazer

# 1
PES_PARA_CM = 30.48
medida_pes = float(input("Médida em pés: "))
medida_cm = medida_pes * PES_PARA_CM
print(f"Conversão: {medida_cm:.1f}")

# 2
medida_pes = float(input("Medida em pés: "))
medida_cm = medida_pes * 30.48
medida_cm = round(medida_cm, 1)
print("Conversão:", medida_cm)

# 3
def pes_para_cm(medida_pes):
    return medida_pes * 30.48

medida_pes = float(input("Médida em pés: "))
medida_cm = pes_para_cm(medida_pes)
print(f"Conversão: {medida_cm:.1f}")

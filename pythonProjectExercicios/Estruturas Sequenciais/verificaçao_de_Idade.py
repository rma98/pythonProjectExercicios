# Criar um algoritmo que pergunte o ano de nascimento do usuário e imprima se ele é de menor.

from datetime import date

ano_Nasc = int(input("Ano de Nascimento:"))
if date.today().year - ano_Nasc >= 18:
    print(True)
else:
    print(False)

# Outras formas de fazer

# 1
from datetime import date

ano_Nasc = input("Ano de Nascimento:")
data_Nasc = date.fromisoformat(f"{ano_Nasc}-01-01")
hoje = date.today()

if (hoje - data_Nasc).days >= 6570: # 6570 dias equivalem a 18 anos
    print(True)
else:
    print(False)

# 2
ano_Nasc = int(input("Ano de Nascimento:"))
idade = 2023 - ano_Nasc

if idade >= 18:
    print(True)
else:
    print(False)

# 3
ano_Nasc = int(input("Ano de Nascimento:"))
maioridade = True if (date.today().year - ano_Nasc >= 18) else False
print(maioridade)

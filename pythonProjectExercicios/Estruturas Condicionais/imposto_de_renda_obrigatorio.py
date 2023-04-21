# Baseado na idade (inteiro) e no salário (real) que o usuário informe, deve mostrar se é ou não obrigatório o
# pagamento do imposto e o valor do imposto que deve ser pago.
# -> Para pagar impostos, o contribuinte deve ter mais de 18 anos e ganhar mais de R$1.903,98.
# -> O valor do imposto devido é de 9,85% do valor do salário.

idade = int(input("Idade: "))
salario = float(input("Salário: R$"))

if idade > 18 and salario > 1903.98:
    porcento = 9.85/100
    imposto = salario * porcento
    salario -= imposto
    print(f"É obrigatório o pagamento do imposto!\nValor do imposto: R${imposto:.2f}\nSalário: R${salario:.2f}")
else:
    print(f"Não é obrigatório!\nSalário: R${salario:.2f}")

# Outras formas de fazer

# 1
def calcular_imposto(idade, salario):
    if idade > 18 and salario > 1903.98:
        porcento = 9.85/100
        imposto = salario * porcento
        salario -= imposto
        print(f"É obrigatório o pagamento do imposto!\nValor do imposto: R${imposto:.2f}\nSalário: R${salario:.2f}")
    else:
        print(f"Não é obrigatório!\nSalário: R${salario:.2f}")

idade = int(input("Idade: "))
salario = float(input("Salário: R$"))
calcular_imposto(idade, salario)

# 2
idade = int(input("Idade: "))
salario = float(input("Salário: R$"))
porcento = 9.85/100

if idade > 18 and salario > 1903.98:
    imposto = salario * porcento
    salario -= imposto
    print(f"É obrigatório o pagamento do imposto!\nValor do imposto: R${imposto:.2f}\nSalário: R${salario:.2f}")
else:
    print(f"Não é obrigatório!\nSalário: R${salario:.2f}")

# 3
idade = int(input("Idade: "))
salario = float(input("Salário: R$"))
impostos = [(0, 1903.98, 0), (1903.99, 2826.65, 7.5/100), (2826.66, 3751.05, 15/100), (3751.06, 4664.68, 22.5/100), (4664.69, float('inf'), 27.5/100)]

for faixa in impostos:
    if idade > 18 and salario > faixa[0] and salario <= faixa[1]:
        porcento = faixa[2]/100
        imposto = salario * porcento
        salario -= imposto
        print(f"É obrigatório o pagamento do imposto!\nValor do imposto: R${imposto:.2f}\nSalário: R${salario:.2f}")
        break
else:
    print(f"Não é obrigatório!\nSalário: R${salario:.2f}")

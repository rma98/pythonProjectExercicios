# Baseado no mês, na idade (inteiro) e no salário (real) que o usuário informe, o algoritmo deve mostrar se é ou não
# obrigatório a contribuição ao sindicato e o valor que deve ser pago. Para contribuir com o sindicato, o contribuinte
# deve ter mais de 25 anos, ganhar mais de R$1345.80 e estar no mês de maio.
# -> O valor da contribuição é de 3.96 do valor do salário.

idade = int(input("Idade: "))
salario = float(input("Salário: "))
mes = input("MêS: ").lower()
if idade > 25 and salario > 1345.80 and mes == "maio":
    porcento = 3.96/100
    desconto = salario * porcento
    novo_Salario = salario - desconto
    print(f"É obrigatório!\n{novo_Salario:.2f}")
else:
    print("Não é obrigatório!")

# Outras formas de fazer

# 1
idade = int(input("Idade: "))
salario = float(input("Salário: "))
mes = input("Mês: ").lower()

if idade > 25 and salario > 1345.80 and mes == "maio":
    desconto = salario * 0.0396
    novo_salario = salario - desconto
    print(f"É obrigatório!\n{novo_salario:.2f}")
else:
    print("Não é obrigatório!")

#2
def verifica_desconto_obrigatorio(idade, salario, mes):
    if idade > 25 and salario > 1345.80 and mes == "maio":
        desconto = salario * 0.0396
        novo_salario = salario - desconto
        print(f"É obrigatório!\n{novo_salario:.2f}")
    else:
        print("Não é obrigatório!")

idade = int(input("Idade: "))
salario = float(input("Salário: "))
mes = input("Mês: ").lower()

verifica_desconto_obrigatorio(idade, salario, mes)

# 3
idade = int(input("Idade: "))
salario = float(input("Salário: "))
mes = input("Mês: ").lower()

desconto_obrigatorio = salario * 0.0396 if idade > 25 and salario > 1345.80 and mes == "maio" else None

if desconto_obrigatorio:
    novo_salario = salario - desconto_obrigatorio
    print(f"É obrigatório!\n{novo_salario:.2f}")
else:
    print("Não é obrigatório!")

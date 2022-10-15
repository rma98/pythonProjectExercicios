#47. João recebeu seu salário e precisa pagar duas contas atrasadas. Por causa do atraso, ele deverá pagar uma multa de
# 2% sobre cada conta. Faça um programa que calcule e mostre quanto restará do salário de João.

salario = float(input("Salário do João: R$"))
contaA = float(input("Conta A: R$"))
contaB = float(input("Conta B: R$"))
multa = 2/100
acrescimoA = contaA * multa
acrescimoB = contaB * multa
contaA += acrescimoA
contaB += acrescimoB
total_A_Pagar = contaA + contaB
print(f"Restará do salário de João um valor de: R${salario - total_A_Pagar:.2f}")

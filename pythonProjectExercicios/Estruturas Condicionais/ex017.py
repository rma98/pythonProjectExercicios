#17. Crie um algoritmo que execute as funcionalidades da conta-corrente de uma pessoa. Toda a conta tem um número, uma
# pessoa vinculada e um saldo. O saldo é atualizado conforme o tipo de movimentação bancária: depósito ou retirada. Se
# for um depósito, o dinheiro é creditado ao saldo; se for retirada, o dinheiro é debitado do saldo.

print("-"*10, "CONTA CORRENTE", "-"*10)
saldo = float(input("Saldo: R$"))
transacao = int(input("1- Depósito\n2- Retirada\n:"))
if transacao == 1:
    deposito = float(input("Depósito: R$"))
    saldo += deposito
    print(f"Saldo: R${saldo:.2f}")
elif transacao == 2:
    debito = float(input("Retirada: R$"))
    saldo -= debito
    print(f"Saldo: R${saldo:.2f}")
else:
    print("Inválido!")

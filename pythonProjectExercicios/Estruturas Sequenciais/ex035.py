#35. Crie um algoritmo que execute as funcionalidades da conta-corrente de uma pessoa. Toda a conta tem um número,
# uma pessoa vinculada a um saldo. O saldo é atualizado conforme o tipo de movimentação bancária: depósito ou retirada.
# Se for um depósito, o dinheiro é creditado ao saldo; se for retirada, o dinheiro é debitado no saldo.

linha = '-'
print(f"{linha*10} CONTA CORRENTE {linha*10}")
numero_Da_Conta = int(input("Número da Conta: "))
saldo = float(input("Saldo em conta: "))
transacao = int(input("1 - Depósito\n2 - Retirada\n:"))
if transacao == 1:
    deposito = float(input("Quanto você que depositar: R$"))
    saldo += deposito
    print(f"Saldo em conta: R${saldo:.2f}")
elif transacao == 2:
    retirada = float(input("Quanto você quer retirar: R$"))
    saldo -= retirada
    print(f"Saldo em conta: R${saldo:.2f}")

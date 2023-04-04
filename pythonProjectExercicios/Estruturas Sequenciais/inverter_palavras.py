# Pergunte ao usuário duas palavras, depois imprima as palavras na ordem contrária â alfabética.

palavra1 = input("Primeira palavra: ")
palavra2 = input("Segunda palavra: ")
print(f"Ordem contrária:\n{palavra1[::-1]}\n{palavra2[::-1]}")

# Outras formas de fazer

# 1
palavra1 = input("Primeira palavra: ")
palavra2 = input("Segunda palavra: ")

print(f"Ordem contrária:\n{''.join(reversed(palavra1))}\n{''.join(reversed(palavra2))}")

# 2
palavra1 = input("Primeira palavra: ")
palavra2 = input("Segunda palavra: ")

print("Ordem contrária:")
for letra in reversed(palavra1):
    print(letra, end='')
print()
for letra in reversed(palavra2):
    print(letra, end='')

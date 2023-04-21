# Pergunte ao usuário duas palavras, depois imprima as palavras na ordem contrária à alfabética.

palavra1 = input("Primeira palavra: ")
palavra2 = input("Segunda palavra: ")
juncao = palavra1 + " " + palavra2
print(juncao)
ordem_Contraria = juncao[::-1]
print(f"Ordem contrária à alfabética: {ordem_Contraria}")

# Outras formas de fazer

# 1
palavras = [input("Digite a primeira palavra: "), input("Digite a segunda palavra: ")]
juncao = " ".join(palavras)
print(juncao)
ordem_Contraria = juncao[::-1]
print(f"Ordem contrária à alfabética: {ordem_Contraria}")

# 2
entrada = input("Digite as duas palavras separadas por espaço: ")
palavras = entrada.split()
juncao = " ".join(palavras)
print(juncao)
ordem_Contraria = juncao[::-1]
print(f"Ordem contrária à alfabética: {ordem_Contraria}")

# 3
palavra1 = input("Primeira palavra: ")
palavra2 = input("Segunda palavra: ")
juncao = palavra1 + " " + palavra2
print(juncao)
ordem_Contraria = juncao[::-1]
print("Ordem contrária à alfabética: {}".format(ordem_Contraria))

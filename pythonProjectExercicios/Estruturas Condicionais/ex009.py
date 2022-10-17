#9. Pergunte ao usuário duas palavras, depois imprima as palavras na ordem contrária à alfabética.

palavra1 = input("Primeira palavra: ")
palavra2 = input("Segunda palavra: ")
juncao = palavra1 + " " + palavra2
print(juncao)
ordem_Contraria = juncao[::-1]
print(f"Ordem contrária à alfabética: {ordem_Contraria}")

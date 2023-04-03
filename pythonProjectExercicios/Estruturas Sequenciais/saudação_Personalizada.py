# Perguntar o nome do usuário e dar "Boa tarde" a essa pessoa.

nome = input("Qual é o seu nome? ")
print(f"Boa tarde, {nome}!")

# Outras formas de fazer

# 1
nome = input("Qual é o seu nome? ")
print("Boa tarde, " + nome + "!")

# 2
nome = input("Qual é o seu nome? ")
mensagem = "Boa tarde, " + nome + "!"
print(mensagem)

# 3
def saudar(nome):
    return "Boa tarde, " + nome + "!"

nome = input("Qual é o seu nome? ")
print(saudar(nome))

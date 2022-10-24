# Laços de Repetição e Listas

print("Carregando")
print("Carregando")
print("Carregando")
print("#####################")
for palavra in range(1, 4):
  print("Carregando")

for item in range(1, 21, 2):
  print(item)

nomes = ["Robson", "Roberto", "Camila", "Pedro"]

for nome in nomes:
  print(nome)


#Problema 1 a N - Imprima os valores de 1 a N

valor_maximo = int(input("Digite o valor máximo: "))
valor_inicial = 1
for numero in range(valor_inicial, valor_maximo+1):
  print(numero)
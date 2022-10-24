# Variáveis

# Números
velocidade_internet = 10
print(velocidade_internet)
nota_filme = 8.5 #float
# Valores Boleanos
esta_aberto = True
# Strings
nome_do_curso = "Lógica de Programação"

#Como variáveis seriam usadas num programa real?

#Escreva um programa que retorna o valor hora de um funcionário com base no seu salário mensal e horas trabalhadas por mês.

salario_mensal = float(input("Qual é o seu salário mensal? R$"))
horas_trabalhadas = float(input("Quantas horas trabalhadas por mês? "))
valor_hora = salario_mensal / horas_trabalhadas
print(f"R${valor_hora:.2f}")
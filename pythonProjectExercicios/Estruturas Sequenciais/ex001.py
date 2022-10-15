#1. Desenvolva um programa que calcule o salário líquido de um Profissional. Para elaborar o programa,
# é necessário possuir alguns dados, tais como: valor da hora aula, número de horas trabalhadas no mês e
#percentual de desconto do INSS. Em primeiro lugar, deve-se estabelecer o seu salário bruto para fazer o desconto e
# depois ter o valor do salário líquido.

valor_Hora_Aula = float(input("Valor da Hora Aula: R$"))
num_Horas_Trabalhadas = int(input("Horas Trabalhadas: "))
percen_Desconto_Inss = int(input("Percentual de desconto: "))
salario_Bruto = valor_Hora_Aula * num_Horas_Trabalhadas
desc = salario_Bruto * percen_Desconto_Inss/100
print(f"Salário bruto: R${salario_Bruto:.2f}\n"
      f"Salário líquido: R${salario_Bruto - desc:.2f}")

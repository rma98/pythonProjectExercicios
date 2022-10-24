# Condicionais
# if, elif, else

'''
E ae Robson, bora dar uma saída hoje?
Se eu terminar meu trabalho aqui, eu consigo.
'''

trabalho_terminado = False
if trabalho_terminado == True:
  print("Opa! Bora dar uma saída.")
else:
  print("Não posso sair agora.")

'''
Ei você consegue me ajudar a mover essas caixas lá para fora hoje a tarde? Se eu estiver livre, sim. Mas se não der pede a meu irmão para te ajudar.
'''

estou_livre = True
if estou_livre == True:
  print("Ok! Posso ajudar hoje sim.")
else:
  print("Peça ao meu irmão para te ajudar!")

'''
Eu cheguei atrasado na aula, ainda posso entrar? Se essa não for sua terceira vez chegando atrasado, então pode sim, caso contrário irá tomar uma suspensão.
'''

numero_de_atrasos = 0
if numero_de_atrasos >=3:
  print("Você está suspenso!")
elif numero_de_atrasos == 1:
  print("Pode entrar, porém tome mais duas faltas será suspenso.")
elif numero_de_atrasos == 2:
  print("Pode entrar, porém tome mais uma falta será suspenso.")
else:
  print("Pode entrar!")

#Encontre o maior entre dois números

primeiro_valor = int(input("Digite o primeiro valor: "))
segundo_valor = int(input("Digite o primeiro valor: "))
if primeiro_valor > segundo_valor:
  print("O primeiro valor é maior!")
else:
  print("O segundo valor é maior!")
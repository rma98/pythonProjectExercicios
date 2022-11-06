#5. Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dadoo. Transfira todas as
# funções utilizadas nos ex001, ex002 e ex003 para o primeiro pacote e matenha tudo funcionando.

from modulos.ex005.utilidadescev import moeda

preco = float(input('Digite o preço: R$'))
moeda.resumo(preco, 35, 22)

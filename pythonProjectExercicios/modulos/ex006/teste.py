#6. Dentro do pacote utilidadesCeV que criamos no ex005, temos um módulo chamado dado. Crie uma função chamada
#leiaDinheiro() que seja capaz de funcionar como a função input(), mas como uma validação de dados para aceitar apenas
# valores que sejam monetários.

from modulos.ex006.utilidadescev import moeda
from modulos.ex006.utilidadescev import dado

preco = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(preco, 35, 22)

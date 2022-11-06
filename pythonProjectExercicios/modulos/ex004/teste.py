#4. Adicione ao módulo moeda.py criado nos ex anteriores, uma função chamada resumo(), que mostre na tela algumas
# informações geradas pelas funções que já temos no módulo criado até aqui.

import moeda

preco = float(input('Digite o preço: R$'))
moeda.resumo(preco, 20, 12)

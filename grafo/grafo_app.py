from grafo import Grafo
from busca_profundidade import BuscaProfundidade
from busca_largura import BuscaLargura

grafo = Grafo()
grafo.arad.mostra_adjacentes()

buscaPronfundidade = BuscaProfundidade(grafo.arad)
buscaPronfundidade.buscar()

buscaLargura = BuscaLargura(grafo.arad)
buscaLargura.buscar()
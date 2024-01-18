from grafo import Grafo
from gulosa import Gulosa
from vetor_ordenado import VetorOrdenado


grafo = Grafo()

vetor = VetorOrdenado(5)
vetor.insere(grafo.arad)
vetor.insere(grafo.craiova)
vetor.insere(grafo.bucharest)
vetor.insere(grafo.dobreta)
vetor.imprime()
print('-------')
vetor.insere(grafo.lugoj)
vetor.imprime()

print(vetor.valores[0], vetor.valores[0].rotulo)

busca_gulosa = Gulosa(grafo.bucharest)
busca_gulosa.buscar(grafo.arad)
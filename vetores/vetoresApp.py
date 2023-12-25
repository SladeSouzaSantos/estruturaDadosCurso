from vetorNaoOrdenado import VetorNaoOrdenado
from vetorOrdenado import VetorOrdenado


def exemploNaoOrdenado(capacidade):
    vetor = VetorNaoOrdenado(capacidade)
    vetor.imprime()

    print("\n--------")
    vetor.insere(2)
    vetor.imprime()

    print("\n--------")
    vetor.insere(3)
    vetor.insere(5)
    vetor.insere(8)
    vetor.insere(1)
    vetor.imprime()

    print("\n--------")
    vetor.insere(7)
    vetor.imprime()

    print("\n--------")
    print(vetor.pesquisar(8))

    print("\n--------")
    print(vetor.pesquisar(3))

    print("\n--------")
    print(vetor.ultima_posicao)

    print("\n--------")
    vetor.excluir(5)
    vetor.imprime()

    print("\n--------")
    vetor.excluir(1)
    vetor.imprime()

    print("\n--------")
    vetor.insere(5)
    vetor.insere(1)
    vetor.imprime()

def exemploOrdenado(capacidade):
    vetor = VetorOrdenado(10)
    
    vetor.insere(6)
    vetor.insere(3)
    vetor.insere(1)
    vetor.imprime()
    
    print("\n--------")
    vetor.insere(4)
    vetor.insere(2)
    vetor.imprime()
    
    print("\n--------")
    vetor.excluir(3)
    vetor.imprime()    
   
print("\n\nVetores Não Ordenados\n")
exemploNaoOrdenado(5)

print("\n\nVetores Ordenados\n")
exemploOrdenado(5)
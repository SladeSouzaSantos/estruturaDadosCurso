from pilha import Pilha


class BuscaProfundidade:
  def __init__(self, inicio):
    self.inicio = inicio
    self.inicio.visitado = True
    self.pilha = Pilha(20)
    self.pilha.empilhar(inicio)

  def buscar(self):
    topo = self.pilha.ver_topo()
    print('Topo: {}'.format(topo.rotulo))
    for adjacente in topo.adjacentes:
      print('Topo é {}. {} já foi visitada? {}'.format(topo.rotulo, adjacente.vertice.rotulo, adjacente.vertice.visitado))
      if adjacente.vertice.visitado == False:
        adjacente.vertice.visitado = True
        self.pilha.empilhar(adjacente.vertice)
        print('Empilhou {}'.format(adjacente.vertice.rotulo))
        self.buscar()
    print('Desempilhou: {}'.format(self.pilha.desempilhar().rotulo))
    print()
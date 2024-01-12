from fila_circular import FilaCircular


class BuscaLargura:
  def __init__(self, inicio):
    self.inicio = inicio
    self.inicio.visitado = True
    self.fila = FilaCircular(20)
    self.fila.enfileirar(inicio)

  def buscar(self):
    primeiro = self.fila.primeiro()
    print('-------')
    print('Primeiro da fila: {}'.format(primeiro.rotulo))
    temp = self.fila.desenfileirar()
    print('Desenfileirou: {}'.format(temp.rotulo))
    for adjacente in primeiro.adjacentes:
      print('Primeiro era {}. {} já foi visitado? {}'.format(temp.rotulo, adjacente.vertice.rotulo, adjacente.vertice.visitado))
      if adjacente.vertice.visitado == False:
        adjacente.vertice.visitado = True
        self.fila.enfileirar(adjacente.vertice)
        print('Enfileirou: {}'.format(adjacente.vertice.rotulo))
    if self.fila.numero_elementos > 0:
      self.buscar()
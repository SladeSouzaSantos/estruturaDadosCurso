from no import No

class NoDuplamenteEncadeada(No):
  def __init__(self, valor):
      super().__init__(valor)
      self.anterior = None
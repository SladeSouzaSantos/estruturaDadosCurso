from no import No

class NoDuplamenteEncadeada(No):
  def __init__(self, valor):
      super().__init__(valor)
      self.anterior = None
      
  def mostrar_encadeamento(self):
    if self == None:
      print("Valor:", None)
    else:
      print("Valor:", self.valor)
    if(self.anterior == None):
      print("Anterior:", None)
    else:
      print("Anterior:", self.anterior.valor)
    if(self.proximo == None):
      print("Proximo: None")
    else:
      print("Proximo:", self.proximo.valor)
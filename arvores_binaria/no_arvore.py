class NoArvore:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        
    def getValor(self):
        return self.valor
    
    def mostrarNo(self):
        print("Valor: ", self.valor)
from listaEncadeadaSimples import ListaEncadeadaSimples
from no import No

class ListaEncadeadaDuplaExtremidade(ListaEncadeadaSimples):
    def __init__(self):        
        super().__init__()
        self.ultimo = None
    
    def insere_inicio(self, valor):
        '''override'''
        novo = No(valor)
        if self.primeiro == None:
            self.ultimo = novo
        novo.proximo = self.primeiro
        self.primeiro = novo
    
    def insere_final(self, valor):
        novo = No(valor)
        if self.primeiro == None:
            self.primeiro = novo
        else: 
            self.ultimo.proximo = novo
        self.ultimo = novo
        
    def excluir_inicio(self):
        if self.primeiro == None:
            print("A lista está vazia")
            return
        
        temp = self.primeiro
        if self.primeiro.proximo == None:
            self.ultimo = None
        self.primeiro = self.primeiro.proximo
        return temp
    
    def excluir_posicao(self, valor):
        if self.primeiro == None:
            print('A lista está vazia')
            return None
        
        atual = self.primeiro
        anterior = self.primeiro
        while atual.valor != valor:
            if atual.proximo == None:
                return None
            else:
                anterior = atual
                atual = atual.proximo
        
        
        if atual == self.primeiro:
            if atual == self.ultimo:
                self.ultimo = self.primeiro.proximo           
            self.primeiro = self.primeiro.proximo        
        else:
            anterior.proximo = atual.proximo
            if atual == self.ultimo:
                self.ultimo = anterior
        
        return atual
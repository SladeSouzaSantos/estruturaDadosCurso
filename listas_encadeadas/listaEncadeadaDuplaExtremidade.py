from listaEncadeadaSimples import ListaEncadeadaSimples
from noDuplamenteEncadeada import NoDuplamenteEncadeada
from no import No

class ListaEncadeadaDuplaExtremidade(ListaEncadeadaSimples):
    def __init__(self):        
        super().__init__()
        self.ultimo = None
    
    def insere_inicio(self, valor, tipoNo = No):
        '''override'''
        if tipoNo == NoDuplamenteEncadeada:
            novo = NoDuplamenteEncadeada(valor)
        else:
            novo = No(valor)
            
        if self.primeiro == None:
            self.ultimo = novo
        elif tipoNo == NoDuplamenteEncadeada:
            self.primeiro.anterior = novo
        
        novo.proximo = self.primeiro
        self.primeiro = novo
    
    def insere_final(self, valor, tipoNo = No):
        if tipoNo == NoDuplamenteEncadeada:
            novo = NoDuplamenteEncadeada(valor)
        else:
            novo = No(valor)
            
        if self.primeiro == None:
            self.primeiro = novo
        else: 
            self.ultimo.proximo = novo
            if tipoNo == NoDuplamenteEncadeada:
                novo.anterior = self.ultimo
        
        self.ultimo = novo
        
    def excluir_inicio(self):
        if self.primeiro == None:
            print("A lista está vazia")
            return
        
        temp = self.primeiro
        
        if self.primeiro.proximo == None:
            self.ultimo = None
        elif hasattr(temp, 'anterior'):
            self.primeiro.proximo.anterior = None
        
        self.primeiro = self.primeiro.proximo
        return temp
    
    def excluir_final(self):
        temp = self.ultimo
        if hasattr(temp, 'anterior'):         
            if self.primeiro.proximo == None:
                self.primeiro = None
            else:
                self.ultimo.anterior.proximo = None
            
            self.ultimo = self.ultimo.anterior
            self.ultimo.mostrar_encadeamento()
            return temp
        else:
            print("Função aplicada somente ao exemplo de No Duplamente Encadeada.")
            return
 
    def excluir_posicao(self, valor):
        if self.primeiro == None:
            print('A lista está vazia')
            return None
        
        atual = self.primeiro
                
        if hasattr(atual, 'anterior'):        
            while atual.valor != valor:
                atual = atual.proximo
                if atual == None:
                    return None
            if atual == self.primeiro:
                self.primeiro = atual.proximo
            else:
                atual.anterior.proximo = atual.proximo
            
            if atual == self.ultimo:
                self.ultimo = atual.anterior
            else:
                atual.proximo.anterior = atual.anterior
        
        else:
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
                if hasattr(anterior, 'anterior'):
                    anterior.anterior = atual.anterior
                if atual == self.ultimo:
                    self.ultimo = anterior
        
        return atual
    
    def mostrar_frente(self):
        atual = self.primeiro
        while atual != None:
            atual.mostra_no()
            atual = atual.proximo

    def mostrar_tras(self):
        atual = self.ultimo
        if hasattr(atual, 'anterior'):            
            while atual != None:
                atual.mostra_no()
                atual = atual.anterior
        else:
            print("Função aplicada somente ao exemplo de No Duplamente Encadeada.")
            return
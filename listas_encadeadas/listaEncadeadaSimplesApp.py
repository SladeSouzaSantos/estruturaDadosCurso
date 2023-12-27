from listaEncadeadaSimples import ListaEncadeadaSimples
from listaEncadeadaDuplaExtremidade import ListaEncadeadaDuplaExtremidade

def exemploListaEncadeadaSimples():
  lista = ListaEncadeadaSimples()
  lista.insere_inicio(1)
  lista.insere_inicio(2)
  lista.insere_inicio(3)
  lista.insere_inicio(4)
  lista.insere_inicio(5)
  lista.mostrar()

  print("-----------")

  lista.excluir_inicio()
  lista.mostrar()

  print("-----------")

  lista.excluir_inicio()
  lista.excluir_inicio()
  lista.mostrar()

  print("-----------")

  lista.excluir_inicio()
  lista.mostrar()

  print("-----------")

  lista.excluir_inicio()
  lista.mostrar()

  print("-----------")

  lista.insere_inicio(1)
  lista.insere_inicio(2)
  lista.insere_inicio(3)
  lista.insere_inicio(4)
  lista.insere_inicio(5)
  lista.mostrar()

  print("-----------")

  pesquisa = lista.pesquisa(3)
  if pesquisa != None:
    print('Encontrado: ', pesquisa.valor)
  else:
    print('Não encontrado')
    
  print("-----------")

  lista.excluir_posicao(3)
  lista.mostrar()

  print("-----------")

  lista.excluir_posicao(1)
  lista.mostrar()

  print("-----------")

  lista.excluir_posicao(2)
  lista.mostrar()

  print("-----------")

  lista.excluir_inicio()
  lista.mostrar()
  
def exemploListaEncadeadaDuplaExtremidade():
  list = ListaEncadeadaDuplaExtremidade()
  list.insere_inicio(1)
  print(list.primeiro, list.ultimo)
  list.insere_inicio(2)
  list.insere_inicio(3)
  list.insere_final(4)
  list.mostrar()
  print(list.primeiro, list.ultimo)
  list.excluir_inicio()
  list.mostrar()
  print(list.primeiro, list.ultimo)
  list.insere_final(5)
  list.mostrar()
  print(list.primeiro, list.ultimo)
  list.excluir_posicao(5)
  list.mostrar()
  print(list.primeiro, list.ultimo)
  list.excluir_posicao(4)
  list.excluir_posicao(2)
  list.mostrar()
  print(list.primeiro, list.ultimo)
  list.excluir_posicao(1)
  list.mostrar()
  print(list.primeiro, list.ultimo)
  list.excluir_inicio()
  list.excluir_posicao(1)
  
print("Lista Encadeada Simples")
exemploListaEncadeadaSimples()
print("Lista Encadeada Dupla Extremidade")
exemploListaEncadeadaDuplaExtremidade()
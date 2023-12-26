from listaEncadeadaSimples import ListaEncadeadaSimples


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

lista.excluir_posicao(5)
lista.mostrar()

print("-----------")

lista.excluir_inicio()
lista.mostrar()
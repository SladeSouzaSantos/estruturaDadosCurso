from arvore_binaria_busca import ArvoreBinariaBusca


arvore = ArvoreBinariaBusca()
arvore.inserir(53)
arvore.inserir(30)
arvore.inserir(14)
arvore.inserir(39)
arvore.inserir(9)
arvore.inserir(23)
arvore.inserir(34)
arvore.inserir(49)
arvore.inserir(72)
arvore.inserir(61)
arvore.inserir(84)
arvore.inserir(79)

print(arvore.raiz.esquerda.valor)
print(arvore.raiz.direita.valor)

print(arvore.ligacoes)

arvore.pesquisar(9)

print(arvore.ligacoes)

arvore.pre_ordem(arvore.raiz)

arvore.excluir(100)

print(arvore.ligacoes)

arvore.excluir(72)

arvore.pesquisar(72)

print(arvore.ligacoes)

arvore.excluir(39)

print(arvore.ligacoes)

arvore.excluir(14)

print(arvore.ligacoes)

arvore.excluir(53)

print(arvore.ligacoes)
arvore.pos_ordem(arvore.raiz)

arvore.excluir(30)

print(arvore.ligacoes)
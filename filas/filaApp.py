from filaCircular import FilaCircular
from filaPrioridade import FilaPrioridade

def exemploFilaCircular():
    print("\n\nFila Circular\n")
    fila = FilaCircular(5)
    print(fila.primeiro())

    fila.enfileirar(1)
    print(fila.primeiro())

    fila.enfileirar(2)
    print(fila.primeiro())

    fila.enfileirar(3)
    fila.enfileirar(4)
    fila.enfileirar(5)
    print(fila.primeiro())

    fila.enfileirar(6)

    fila.desenfileirar()
    fila.desenfileirar()
    print(fila.primeiro())

    print(fila.valores)
    print(fila.inicio, fila.final)
    
def exemploFilaPrioridade():
    print("\n\nFila Prioridade\n")
    fila = FilaPrioridade(5)
    print(fila.primeiro())
    
    fila.enfileirar(30)
    print(fila.primeiro())
    
    fila.enfileirar(50)
    print(fila.primeiro())
    
    fila.enfileirar(10)
    print(fila.primeiro())
    print(fila.valores)
    
    fila.enfileirar(20)
    print(fila.primeiro())
    
    fila.enfileirar(40)
    print(fila.primeiro())
    
    fila.enfileirar(100)
    print(fila.valores)
    
    fila.desenfileirar()
    print(fila.primeiro())
    
    fila.desenfileirar()
    print(fila.primeiro())
    
    fila.desenfileirar()
    print(fila.primeiro())
    
    print(fila.valores)
    
    fila.enfileirar(120)
    print(fila.primeiro())
    print(fila.valores)
    return

exemploFilaCircular()
exemploFilaPrioridade()
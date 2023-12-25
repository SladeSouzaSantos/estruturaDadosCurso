from dequeCircular import DequeCircular
import numpy as np

deque = DequeCircular(5)

deque.insere_final(5)
print(deque.get_inicio(), deque.get_final())

deque.insere_final(10)
print(deque.get_inicio(), deque.get_final())

deque.insere_inicio(3)
print(deque.get_inicio(), deque.get_final())

deque.insere_inicio(2)
deque.insere_final(11)
print(deque.get_inicio(), deque.get_final())

deque.excluir_inicio()
print(deque.get_inicio(), deque.get_final())

deque.excluir_final()
print(deque.get_inicio(), deque.get_final())

print(deque.valores)

a = np.array([[1,2],[3,4]])
b = np.array([[4,5], [8,9]])

print(a.dot(b))
print(b.dot(a))
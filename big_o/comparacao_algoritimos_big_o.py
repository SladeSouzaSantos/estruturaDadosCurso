
import timeit


def soma1(n):
    soma = 0
    for i in range(n + 1):
        soma += i
    return soma


def soma2(n):
    return (n * (n + 1))/2


def lista1():
    lista = []
    for i in range(1000):
        lista += [i]
    return lista


def lista2():
    return range(1000)


def tempo(funct):
    return timeit.timeit(f'{funct}', number=10000000)


tSoma1 = tempo(soma1(100000))
tSoma2 = tempo(soma2(100000))
print(f"t1: {tSoma1} seg. t2: {tSoma2} seg. {round(((tSoma1 - tSoma2)/tSoma1)*100)} %")

tLista1 = tempo(lista1())
tLista2 = tempo(lista2())
print(f"t1: {tLista1} seg. t2: {tLista2} seg. {round(((tLista1 - tLista2)/tLista1)*100)} %")
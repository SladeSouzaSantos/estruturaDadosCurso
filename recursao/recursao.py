def soma(n):
  if n == 0:
    return 0

  return n + soma(n - 1)

def fatorial(n):
  if n == 0:
    return 1
  return n * fatorial(n - 1)

def potencia(base, expoente):
  if expoente == 0:
    return 1

  return base * potencia(base, expoente - 1)

print(soma(5))
print(fatorial(10))
print(potencia(5, 5))
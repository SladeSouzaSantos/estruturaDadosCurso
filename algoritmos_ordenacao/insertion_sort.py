class InsertionSort:
    def insertion_sort(vetor):
        n = len(vetor)

        for i in range(1, n):
            marcado = vetor[i]

            j = i - 1
            while j >= 0 and marcado < vetor[j]:
                vetor[j + 1] = vetor[j]
                j -= 1
            vetor[j + 1] = marcado

        return vetor
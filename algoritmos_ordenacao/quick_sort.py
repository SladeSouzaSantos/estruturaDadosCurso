class QuickSort:
    
    def __init__(self, vetor):
        self.__vetorResult = QuickSort.__quick_sort(vetor, 0, len(vetor) - 1)
    
    def getVetor(self):
        return self.__vetorResult
    
    def __particao(vetor, inicio, final):
        pivo = vetor[final]
        i = inicio - 1

        for j in range(inicio, final):
            if vetor[j] <= pivo:
                i += 1
                vetor[i], vetor[j] = vetor[j], vetor[i]
        vetor[i + 1], vetor[final] = vetor[final], vetor[i + 1]
        return i + 1

    def __quick_sort(vetor, inicio, final):
        if inicio < final:
            posicao = QuickSort.__particao(vetor, inicio, final)
            # Esquerda
            QuickSort.__quick_sort(vetor, inicio, posicao - 1)
            # Direito
            QuickSort.__quick_sort(vetor, posicao + 1, final)
        return vetor
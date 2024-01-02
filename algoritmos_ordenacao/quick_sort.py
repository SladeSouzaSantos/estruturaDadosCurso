class QuickSort:
    
    def particao(vetor, inicio, final):
        pivo = vetor[final]
        i = inicio - 1

        for j in range(inicio, final):
            if vetor[j] <= pivo:
                i += 1
                vetor[i], vetor[j] = vetor[j], vetor[i]
        vetor[i + 1], vetor[final] = vetor[final], vetor[i + 1]
        return i + 1

    def quick_sort(vetor, inicio, final):
        if inicio < final:
            posicao = QuickSort.particao(vetor, inicio, final)
            # Esquerda
            QuickSort.quick_sort(vetor, inicio, posicao - 1)
            # Direito
            QuickSort.quick_sort(vetor, posicao + 1, final)
        return vetor
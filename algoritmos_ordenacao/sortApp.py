import numpy as np
from shell_sort import ShellSort
from insertion_sort import InsertionSort
from bubble_sort import BubbleSort
from selection_sort import SelectionSort

vetor = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Vetor Desordenado:", vetor)
print("Vetor Ordenado (Bubble Sort):", BubbleSort.bubble_sort(np.array(vetor)))
print("Vetor Ordenado (Selection Sort):", SelectionSort.selection_sort(np.array(vetor)))
print("Vetor Ordenado (Insertion Sort):", InsertionSort.insertion_sort(np.array(vetor)))
print("Vetor Ordenado (Shell Sort):", ShellSort.shell_sort(np.array(vetor)))
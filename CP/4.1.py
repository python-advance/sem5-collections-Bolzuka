# 4.1. Создание программы по заполнению массивов случайными значениями. Сортировка значений в списке методом вставки, плавной сортировки, с помощью встроенных функций языка.

import numpy as np
import numpy.random 

print("Рандомный массив")
a = np.random.randint(0, 100, 10)
print(a)
print()

print("С помощью встроенных функций языка")
sortarray0 = a
sortarray0.sort()
print(sortarray0)
print()

print("Сортировка по возростанию")
sortarray1 = sorted(a)
print(sortarray1)
print()

print("Сортировка по убыванию")
sortarray2 = sorted(a, reverse = True)
print(sortarray2)
print()

print("Сортировка значений в списке методом вставки")
def sortarray3(a):
	for i in range(len(a) - 1):
		j = i - 1 
		key = a[i]
		while a[j] > key and j >= 0:
			a[j + 1] = a[j]
			j -= 1
		a[j + 1] = key
	return a
print(sortarray3(a))
print()

print("Плавная сортировка")

def sortarray4(a):
    """Сортирует список в возрастающем порядке с помощью алгоритма пирамидальной сортировки"""
  
    def downHeap(a, k, n):
        new_elem = a[k]
        while 2*k+1 < n:
            child = 2*k+1
            if child+1 < n and a[child] < a[child+1]:
                child += 1
            if new_elem >= a[child]:
                break
            a[k] = a[child]
            k = child
        a[k] = new_elem
  
    size = len(a)
    for i in range(size//2-1,-1,-1):
        downHeap(a, i, size)
    for i in range(size-1,0,-1):
        temp = a[i]
        a[i] = a[0]
        a[0] = temp
        downHeap(a, 0, i)
    return a

print(sortarray4(a))
print()

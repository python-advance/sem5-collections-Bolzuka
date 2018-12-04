# 4.2. Создание программы по распределению списка с случайными значениями на два списка по определенному критерию (четность/нечетность, положительные/отрицательные числа).

import numpy as np
import numpy.random 

print("Рандомный массив")
a = np.random.randint(-50, 50, 10)
print(a)
print()

print("Четный список")
sortarray1 = []
i = 0
while i < 10:
	if a[i]%2 == 0:
		sortarray1.append(a[i])
	i += 1
print(sortarray1)
print()

print("Нечетный список")
sortarray2 = []
i = 0
while i < 10:
	if a[i]%2 == 1:
		sortarray2.append(a[i])
	i += 1
print(sortarray2)
print()

print("Положительные")
sortarray3 = []
i = 0
while i < 10:
	if a[i] > 0:
		sortarray3.append(a[i])
	i += 1
print(list(sortarray3))
print()

print("Отрицательные")
sortarray4 = []
i = 0
while i < 10:
	if a[i] < 0:
		sortarray4.append(a[i])
	i += 1
print(list(sortarray4))
print()

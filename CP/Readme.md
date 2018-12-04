### Отчет 

# 4.1. Создание программы по заполнению массивов случайными значениями. 
Сортировка значений в списке методом вставки, плавной сортировки, с помощью встроенных функций языка.

Импортируем 
```python
import numpy as np
import numpy.random
```
 
Выводим массив из 10 чисел с рандомными числами от 0 до 100 

```
print("Рандомный массив")
a = np.random.randint(0, 100, 10)
print(a)
print()
```

Сортировка с помощью встроенных функций языка 
sort() и sorted

```
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
```

Сортировка значений в списке методом вставки

```
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
```


Плавная сортировка
Сортирует список в возрастающем порядке с помощью алгоритма пирамидальной сортировки

```
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
```

Вывод: 

![Скрин 1](https://github.com/python-advance/sem5-collections-Bolzuka/blob/master/CP/4.1.png "Скрин 1")







# 4.2. Создание программы по распределению списка с случайными значениями на два списка по определенному критерию (четность/нечетность, положительные/отрицательные числа).

Снова импортируем модули
Снова выводим массив из 10 чисел с рандомными числами от -50 до 50 

```
print("Рандомный массив")
a = np.random.randint(-50, 50, 10)
print(a)
print()
```

Выводим четные элементы массива
```
print("Четный список")
sortarray1 = []
i = 0
while i < 10:
	if a[i]%2 == 0:
		sortarray1.append(a[i])
	i += 1
print(sortarray1)
print()
```

Выводим нечетные элементы массива
```
print("Нечетный список")
sortarray2 = []
i = 0
while i < 10:
	if a[i]%2 == 1:
		sortarray2.append(a[i])
	i += 1
print(sortarray2)
print()
```

Выводим положительные элементы массива
```
print("Положительные")
sortarray3 = []
i = 0
while i < 10:
	if a[i] > 0:
		sortarray3.append(a[i])
	i += 1
print(list(sortarray3))
print()
```

Выводим отрицательные элементы массива
```
print("Отрицательные")
sortarray4 = []
i = 0
while i < 10:
	if a[i] < 0:
		sortarray4.append(a[i])
	i += 1
print(list(sortarray4))
print()
```

Вывод: 

![Скрин 2](https://github.com/python-advance/sem5-collections-Bolzuka/blob/master/CP/4.2.png "Скрин 2")


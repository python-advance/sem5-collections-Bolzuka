# 4.3. Создание программы, позволяющей выполнять основные операции (объединение, пересечение, вычитание) над множествами (количество множеств и их элементы вводятся вручную).

def get_arrays(count: int):
    i = 1
    arrays = []
    while i <= count:
        a = input("Введите множество " + str(i) + ": ")
        a = a.split(",")
        for j in range(len(a)):
            a[j] = int(a[j])
        arrays.append(a)
        i += 1
    return arrays

def culculate():
    """
    функция для калькулятора множеств
    """
    print('Инструкция: ')
    print('1) Введите колличество множеств')
    print('2) Введите множества по очереди, поэлементно, разделяя элементы запятой')

    arrays_count = int(input(' Введите количество множеств: \n'))
    word = input(' Введите номер действия: \n 1.Объединение, 2.Пересечение, 3.Разность\n').upper()

    if word == '1':
        arrays = get_arrays(arrays_count)
        result = set(arrays[0])
        for i in range(1, len(arrays)):
            result |= set(arrays[i])
        print("Ответ:", result)
    elif word == '2':
        arrays = get_arrays(arrays_count)
        result = set(arrays[0])
        for i in range(1, len(arrays)):
            result &= set(arrays[i])
        print("Ответ:", result)
    elif word == '3':
        arrays = get_arrays(arrays_count)
        result = set(arrays[0])
        for i in range(1, len(arrays)):
            result -= set(arrays[i])
        print("Ответ:", result)
    else:
        print('Попробуйте еще раз :)')


culculate()



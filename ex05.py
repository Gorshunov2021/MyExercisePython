# ЗАДАНИЕ 3 УПРАЖНЕНИЕ 4 - Найти значение минимального элемента списка.

import random

# Введу размер списка n с клавы
n = int(input("Введите размер списка: \n"))
A = []  # Создание пустого списка целых чисел
for i in range(n):
    a = random.randint(0, 100)  # генерация случайного целого числа
    A.append(a)  # добавление числа в список
# Сдесь происходит обработка
s = sum(A)
l = len(A)
a = s / l
print("Рандомные элементы списка A: ")
for i in range(n):
    print(A[i])

# задаем список
B = list(A)
# предположим, что максимальный элемент равен B[0]
minimum = B[0]
for i in range(1, len(B)):
    if B[i] < minimum:
        minimum = B[i]
print("Минимальное значение элементов списка: " + str(minimum))


# Для поиска максимального элемента списка необходимо заменить знак на > (больше)

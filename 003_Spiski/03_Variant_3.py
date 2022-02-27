# Найдите сумму отрицательных элементов списка.
import random

print("Сгенерируем случайные числа: ")
main_arr = [random.randint(-100, 200) for i in range(35)]
print(main_arr)
print("")

arr_odd = [j for j in main_arr if j < 0]
arr_even = [j for j in main_arr if j >= 0]

print(f'Нечётные числа из этого списка:{arr_odd}\nЧётные числа из этого списка:{arr_even}')
print("")
print("Сумма отрицательных чисел списка: ")
print(sum(arr_odd))

print("")
print("Сумма положительных чисел списка: ")
print(sum(arr_even))

# Задание 2. Задачи на многомерные списки
# Вариант 3. Даны две квадратных таблицы чисел. Требуется построить третью,
# каждый элемент которой равен сумме элементов, стоящих на том же
# месте в 1-й и 2-й таблицах.

# ## РЕШЕНИЕ
import random
import numpy as np

first = 0  # указываем НАЧАЛЬНОЕ число диапазона знач для  матриц
last = 70  # указываем ПОСЛЕДНЕЕ число диапазона знач для  матриц
s = 5  # размер матрицы
matrixs = []  # инициализация списка для матриц

n = 1
for j in range(2):
    n = np.array([[random.randrange(first, last) for i in range(s)] for i in range(s)])  # заполнняем матрицы рандомно
    matrixs.append(n)
    print("\n Матрица " + str(j + 1) + "\n" + str(n))

sumtrx = sum(matrixs)
print("\n Матрица 3 показывает сумму 1-ой и 2-ой матриц поэлементно \n " + str(sumtrx))

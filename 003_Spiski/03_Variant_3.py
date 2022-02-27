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
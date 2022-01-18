# Реализуйте рекурсивную функцию нарезания прямоугольника
# с заданными пользователем сторонами a и b на квадраты с наибольшей возможной на каждом этапе стороной.
# Выведите длины ребер получаемых квадратов и кол-во полученных квадратов.

a = int(input("Сторона а=\n"))
b = int(input("Сторона b=\n"))

def rectangle(a, b, n=0):
    if a == b:
        return n + 1
    elif a < b:
        return rectangle(a, b - a, n + 1)
    return rectangle(a - b, b, n + 1)

print(f"Прямоугольнику с длинами {a} и {b} можно нарезать {rectangle(a, b)} квадратов")


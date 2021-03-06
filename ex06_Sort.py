import random
import datetime
import prettytable  # пакет для таблицы
import matplotlib.pyplot as plt  # библиотека для графика


# def BubbleSort(A):                  # сортировка пузырьком
#     for i in range(len(A)):
#         for j in range(len(A)-1-i):
#             if A[j] > A[j+1]:
#                 a = A[j]
#                 A[j] = A[j+1]
#                 A[j+1] = a

def BubbleSort(Z):                    # сортировка коктельная (SHAKER)
    for i in range(0, len(Z)//2):
        for j in range(i, len(Z)-1-i):
            if Z[j] > Z[j+1]:
                z = Z[j]
                Z[j] = Z[j+1]
                Z[j+1] = z
        for j in range(len(Z)-2-1, i+1):
            if Z[j] < Z[j-1]:
                z = Z[j]
                Z[j] = Z[j - 1]
                Z[j - 1] = z


# def BubbleSort(nums):                  # сортировка вставками (InsertSort)
#     for i in range(1, len(nums)):
#         t = nums[1]
#         j=i
#         while j>=0 and nums[j-1] >t:
#             nums[j] = nums[j - 1]
#             j-=1
#             nums[j] = t

# def BubbleSort(N):                   # сортировка вставками (выбором (select))
#    for i in range(0, len(N) - 1):
#        smallest = i
#        for j in range(i + 1, len(N)):
#            if N[j] < N[smallest]:
#                smallest = j
#        N[i], N[smallest] = N[smallest], N[i]


def QuickSort(A, fst, lst):  # быстрая сортировка
    if fst >= lst:
        return

    # i, j = fst, lst
    pivot = A[fst]
    # pivot = A[random.randint(fst, lst)]
    first_bigger = fst + 1
    while first_bigger <= lst:
        if A[first_bigger] >= pivot:
            break
        first_bigger += 1
    i = first_bigger + 1
    while i <= lst:
        if A[i] < pivot:
            A[i], A[first_bigger] = A[first_bigger], A[i]
            first_bigger += 1
        i += 1

    last_smaller = first_bigger - 1
    A[fst], A[last_smaller] = A[last_smaller], A[fst]
    QuickSort(A, fst, last_smaller - 1)
    QuickSort(A, first_bigger, lst)


table = prettytable.PrettyTable(["Размер списка", "Время пузырька", "Время быстрой"])
x = []
y1 = []
y2 = []

for N in range(1000, 5001, 1000):
    x.append(N)
    min = 1
    max = N
    A = []
    for i in range(N):
        A.append(int(round(random.random() * (max - min) + min)))

    # print(A)

    B = A.copy()
    # print(B)

    # BubbleSort(A)
    print("---")
    # print(A)

    # QuickSort(B, 0, len(B)-1)
    print("---")
    # print(B)

    t1 = datetime.datetime.now()
    BubbleSort(A)
    t2 = datetime.datetime.now()
    y1.append((t2 - t1).total_seconds())
    print("Пузырьковая сортировка   " + str(N) + "   заняла   " + str((t2 - t1).total_seconds()) + "c")

    t3 = datetime.datetime.now()
    QuickSort(B, 0, len(B) - 1)
    t4 = datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    print("Быстрая   " + str(N) + "   заняла   " + str((t4 - t3).total_seconds()) + "c")

    table.add_row([str(N), str((t2 - t1).total_seconds()), str((t4 - t3).total_seconds())])
print(table)

plt.plot(x, y1, "C0")
plt.plot(x, y2, "C1")
plt.show()

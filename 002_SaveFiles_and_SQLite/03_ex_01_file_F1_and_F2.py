"""Предварительно создать текстовый файл F1 не менее чем из 10 строк и записать в него информацию."""

"""Exercise 01"""
"""Скопировать в файл F2 только четные строки из F1. Подсчитать размер файлов F1 и F2 (в байтах)."""

import os

with open("F1.txt", "w", encoding="utf-8") as file1:
    file1.write("Python — высокоуровневый язык программирования общего назначения.\n"
                "с динамической строгой типизацией и автоматическим управлением памятью\n"
                "ориентированный на повышение производительности разработчика,\n"
                "читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ\n"
                "Язык является полностью объектно-ориентированным в том плане, что всё является объектами\n"
                "с динамической строгой типизацией и автоматическим управлением памятью\n"
                "Необычной особенностью языка является выделение блоков кода пробельными отступами\n"
                "Синтаксис ядра языка минималистичен,\n"
                "за счёт чего на практике редко возникает необходимость обращаться к документации\n"
                "Сам же язык известен как интерпретируемый и используется в том числе для написания скриптов\n"
                "Недостатками языка являются зачастую более низкая скорость работы и\n"
                "более высокое потребление памяти написанных на нём программ по сравнению с аналогичным кодом,\n"
                "написанным на компилируемых языках, таких как C или C++")

file2 = open("F2.txt", "w")

with open("F1.txt", "r", encoding="utf-8") as file1:
    All_lines = file1.readlines()  # Чтение всех строк из файла file1

file2.writelines(All_lines[1::2])  # запишим только четный строки. Если вместо двойки будет тройка, то каждую третью

print(os.path.getsize("F1.txt"))
print(os.path.getsize("F2.txt"))

# file1.close()
file2.close()


# Просто проверяю код...
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -9, 45]
print(my_list[1:7:2])

my_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -9, -45]
print(my_list[1::2])
# странно, почему выводит 45 вместо -45    ????
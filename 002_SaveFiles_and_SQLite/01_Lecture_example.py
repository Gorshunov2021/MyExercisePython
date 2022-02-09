# n = input("Введите целое число: ")
# try:
#     n = int(n)
#     print("Удачно")
# except:
#     print("Что-то пошло не так")
#
# try:
#    n = input('Введите целое число: ')
#    n = int(n)
#    print("Все нормально. Вы ввели число", n)
# except ValueError:
#    print("Вы ввели не целое число")


# try:
#     a = float(input("Введите делимое: "))
#     b = float(input("Введите делитель: "))
#     c = a / b
#     print("Частное: ", c)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")


try:
   n = input('Введите целое число: ')
   n = int(n)
except ValueError:
   print("Вы что-то попутали с вводом!")
else:
    print("Все нормулики. Вы ввели число", n)
finally:
   print("Конец программы")
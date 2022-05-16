from full_name import full_name

print("Для остановки теста введите символ 'Q'")
while True:
    first = input("\nВведите Ваше Имя: ")
    if first == 'Q':
        break
    last = input("\nВведите Вашу Фамилию: ")
    if last == 'Q':
        break
    format_name = full_name(first, last)
    print("\nФорматирование Имени:  " + format_name)

# task 1 exercise 4 - По номеру месяца напечатать пору года.
# Вариант 1 - через if-elif-else

weather = int(input("Enter the month number:\n"))

if weather == 1:
    print("Winter time")
elif weather == 2:
    print("Winter time")
elif weather == 3:
    print("Spring time")
elif weather == 4:
    print("Spring")
elif weather == 5:
    print("Spring time")
elif weather == 6:
    print("Summer time")
elif weather == 7:
    print("Summer time")
elif weather == 8:
    print("Summer time")
elif weather == 9:
    print("Autumn time")
elif weather == 10:
    print("Autumn time")
elif weather == 11:
    print("Autumn time")
elif weather == 12:
    print("Winter time")
else:
    print(str(weather) + " - There is no such month!")

# Вариант 2 - через if-elif-else только сокращенно

print("Еще разок! Так как другой код")

weather2 = int(input("Enter the month number:\n"))

if weather2 == 12 or weather2 == 1 or weather2 == 2:
    print("Winter time")

elif weather2 == 3 or weather2 == 4 or weather2 == 5:
    print("Spring time")

elif weather2 == 6 or weather2 == 7 or weather2 == 8:
    print("Summer time")

elif weather2 == 9 or weather2 == 10 or weather2 == 11:
    print("Autumn time")

elif weather2 == 0 or weather2 > 12:
    print(str(weather) + " - There is no such month!")

print("***********************************************************")


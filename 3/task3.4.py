import random
a = 3
while a > 0:
    number1 = random.randint(0, 999)
    number2 = random.randint(0, 999)
    answer = int(input("Вычислете " + f"{number1} / {number2} = "))
    if answer == int(number2 + number1):
        print("Молодец, игра продолжается")
    else:
        a = a - 1
        print("Ошибка")
print ("Игра окончена")

def task1():
    import random
    num = []
    for i in range(5):
        num.append(random.randint(1, 10))
    n = int(input("Угадайте число из списка"))
    if n == num:
        print("Ура! Вы угадали число. Cписок чисел: ", num, "Ваше число: ", n)
    else:
        print("Нет такого числа! Cписок чисел: ", num, "Ваше число: ", n)

def task2():
    import random
    x = []
    for i in range(5):
        x.append(random.randint(1,12))
    print(x)
    for n in x:
        if x.count(n) > 1:
            print("повторяющиеся значения: ", n)
        else:
            print("повторяющихся значений нет")
def task3():
    x = ("Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс")
    y = int(input("Сколько выходных вы хотите?"))
    z = x[-y:]
    m = 7 - y
    n = x[:m]
    print("Ваши вых. дни: ", z)
    print("Ваши раб. дни", n)
task3()


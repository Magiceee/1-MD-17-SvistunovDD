
def f1(x):
    if x % 7 == 0:
        print("число делится на 7")
    else:
        print("число не делится на 7")

def f2(x):
    n2 = 200 / x
    return n2
try:
    a = int(input("введите число"))
    print(f2(a))
except ZeroDivisionError:
    print("деление на ноль невозможно")
except ValueError:
    print("неверное значение числа")


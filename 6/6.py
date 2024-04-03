def task1():
    countries = {'Россия':'Москва', "Англия":"Лондон", "Германия":"Берлин", 'Япония':'Токио', 'Франция':"Париж", 'Америка':'Вашингтон'}
    def a():
        print(countries)
    a()

    def b():
        country = input("Введите любую страну: ")
        if country in countries:
            capital = countries[country]
            print(capital)
        else:
            print("Такой страны нет в списке или она не существует")
    b()

    def c():
        alph = list(countries.keys())
        alph.sort()
        for i in alph:
            print(i, ":", countries[i])
    c()



def task2():
    game = {"А":1, "В":1, "Е":1, "Н":1, "И":1, "С":1, "Р":1, "О":1, "Т":1, "Д":2, "К":2, "Л":2, "М":2, "П":2, "У":2, "Й":4, "Ы":4, "Ж":5, "З":5, "Х":5, "Ц":5, "Ч":5, "Б":3, "Г":3, "Ё":3, "Ь":3, "Я":3, "Ш":8, "Ю":8, "Е":8, "Ф":10, "Щ":10, "Ю":10}
    word = input("Введите слово: ")
    x = list(word)
    score = 0
    for i in x:
        score += 2 * game[i]
    print(score)

task2()


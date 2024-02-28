a = int(input("введите число слов"))
allwords = str()
while a != 0:
    word = input("напишите любое слово")
    allwords = allwords + " " + word
    a = a - 1
    if a == 0:
        break
print(str(allwords))
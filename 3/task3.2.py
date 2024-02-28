a = str()
allwords = str()
word = str()
while word != "стоп":
    word = input("напишите любое слово")
    if word != "стоп":
        allwords = allwords + " " + word
print(str(allwords))
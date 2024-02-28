word = str()
while word != "стоп":
    word = input("напишите любое слово")
    if "ф" in word:
        print ("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")
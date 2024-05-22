import os, csv
from PIL import Image, ImageFilter

def task1():
    dirin = 'dir_in'
    dirout = 'dir_out'

    for filename in os.listdir(dirin):
        pathin = os.path.join(dirin, filename)
        pathout = os.path.join(dirout, filename)

        img = Image.open(pathin)
        filtr_img = img.filter(ImageFilter.FIND_EDGES)
        filtr_img.save(pathout)

def task2():
    dirin = 'dir_in'
    dirout = 'dir_out'

    for name in os.listdir(dirin):
        pathin = os.path.join(dirin, name)
        pathout = os.path.join(dirout, name)

        if os.path.isfile(pathin) and name.endswith(('.jpg', '.png')):
            img = Image.open(pathin)
            filtr_img = img.filter(ImageFilter.FIND_EDGES)
            filtr_img.save(pathout)


def task3():
    sum = 0
    with open('file.csv', 'w', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        print('Нужно купить:')
        for row in reader:
            amount = int(row[1])
            price = int(row[2])
            sum += amount * price

            print(f'{row[0]} - {amount} штук за {price} рублей')

        print(f'Итог, сумма: {sum} рублей')
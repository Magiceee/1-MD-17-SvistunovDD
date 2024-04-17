from PIL import Image, ImageFilter
def task1():
    img = Image.open("Волк.jpg")
    img.show()
    print(f"Размер: {img.size}", f"Формат: {img.format}", f"Цветовая модель: {img.mode}")

def task2():
    img = Image.open("Волк.jpg")
    reds_img = img.reduce(3)
    reds_img.save('Волчара.jpg')
    rotd_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    rotd_img.save('Волчара_правый.jpg')
    rotd_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    rotd_img.save('Волчара_верховный.jpg')

def task3():
    imgs = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']
    for img in imgs:
        image = Image.open(img)
        eff_img = image.filter(ImageFilter.EMBOSS)
        eff_img.save('Фильтры.jpg' + str(img))


task3()
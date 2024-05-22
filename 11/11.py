def task1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Ресторан: {self.restaurant_name}")
            print(f"Кухня: {self.cuisine_type}")

        def open_restaurant(self):
            print(f"{self.restaurant_name} открыт")

    newrestaurant = Restaurant("Сакура", "Японская")

    newrestaurant.describe_restaurant()
    newrestaurant.open_restaurant()

def task2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Ресторан: {self.restaurant_name}")
            print(f"Кухня: {self.cuisine_type}")

    newrestaurant1 = Restaurant("Сакура", "Японская")
    newrestaurant2 = Restaurant("Марио", "Итальянская")
    newrestaurant3 = Restaurant("Бобр", "Польская")

    newrestaurant1.describe_restaurant()
    newrestaurant2.describe_restaurant()
    newrestaurant3.describe_restaurant()


task2()
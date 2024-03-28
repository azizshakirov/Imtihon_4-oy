import datetime


class Product:
    def __init__(self, name, price, year_create):
        self.name = name
        self.price = price
        self.year_create = year_create

class Licence_product(Product):
    def __init__(self, name, price, year_create, data_price):
        super().__init__(name, price, year_create)
        self.data_price = data_price

products = []
for i in range(5):
    name = input(f"Obyekt {i+1}ning nomi: ")
    price = float(input(f"Obyekt {i+1}ning narxi: "))
    year_create = int(input(f"Obyekt {i+1}ning yaratilgan yili: "))
    data_price = input(f"Obyekt {i+1}ning malumoti: ")
    products.append(Licence_product(name, price, year_create, data_price))

today = datetime.date.today()

for i, product in enumerate(products, start=1):
    years_passed = today.year - product.year_create
    print(f"Obyekt {i}: {years_passed} kun o'tgan")
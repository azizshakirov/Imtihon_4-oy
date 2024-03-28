class Book:
    def __init__(self, name, author, year):
        self.Name = name
        self.Author = author
        self.Year = year

class BookStore(Book):
    def __init__(self, name, author, year, price):
        super().__init__(name, author, year)
        self.Price = price

    def discounted_price(self):
        current_year = 2024
        years_passed = current_year - self.Year
        if years_passed >= 5:
            discount = 0.2 
            discounted_price = self.Price - (self.Price * discount)
            return discounted_price
        else:
            return self.Price
        
bookstore_objects = []
for i in range(5):
    name = input(f"{i+1}-kitobni nomini kiriting : ")
    author = input(f"{i+1}-kitobni muallifini kiriting: ")
    year = int(input(f"{i+1}-kitobni yilini kiriting: "))
    price = float(input(f"{i+1}-kitobni narxini kiriting: "))
    bookstore_objects.append(BookStore(name, author, year, price))

for obj in bookstore_objects:
    discounted_price = obj.discounted_price()
    print(f" {obj.Name} >>> {discounted_price}")

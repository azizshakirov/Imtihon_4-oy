class Book:
    def __init__(self, name, page_count, price) -> None:
        self.name = name
        self.page_count = page_count
        self.price = price

    def __str__(self) -> str:
        return f"""
    ****Book****
    Name: {self.name}
    Pages: {self.page_count}
    Price: {self.price}
"""
    def addBooks():
        books = []
        for _ in range(5):
            nomi = input("Kitob nomi: ")
            bet = int(input("Kitob betlari soni: "))
            narx = int(input("Narxi: "))
            books.append(Book(nomi, bet, narx))
            print("\n")
        return books

    def add_ten_pages(self):
        self.page_count += 10
        return self.page_count
    
    def price_update(self):
        if self.page_count > 100:
            self.price //= 2

books = Book.addBooks()

for i in books:
    i.add_ten_pages()
    i.price_update()
    print(i)
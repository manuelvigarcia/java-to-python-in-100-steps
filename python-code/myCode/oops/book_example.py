class Book:
    def __init__(self, name, number_of_copies = 1):
        self.name = name
        self.number_of_copies = number_of_copies

    def __repr__(self):
        return repr((self.name, self.number_of_copies))


    def increase_number_of_copies(self, how_many = 1):
        self.number_of_copies += how_many


    def decrease_number_of_copies(self, how_many=1):
        self.number_of_copies -= how_many


book1 = Book("Mastering Spring 5.0", 5)
book2 = Book("Mastering Python")

book1.increase_number_of_copies(1)
book1.increase_number_of_copies(2)
book2.increase_number_of_copies(5)
book2.increase_number_of_copies(2)

print(book1)
print(book2)



class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __repr__(self):
        return repr((self.name, self.address))

class Student(Person):
    def __init__(self, name, address, college_name, year):
        super().__init__(name, address)
        self.college_name = college_name
        self.year = year

    def __repr__(self):
        return repr((super().__repr__(),self.college_name, self.year))

person = Person ("Manuel", "Narón")

student = Student("Manuel", "Narón", "Ferrol Campus Propulsion", "3º")

print(person)

print(student)
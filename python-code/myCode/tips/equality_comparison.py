#overloading __eq__ operator.

class Money:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __add__(self, other):
        return Money(self.currency, self.amount + other.amount)

    def __sub__(self, other):
        return Money(self.currency, self.amount - other.amount)

    def __eq__(self, other):
        return (self.currency, self.amount) == (other.currency, other.amount)

    def __gt__(self, other):
        return (self.currency, self.amount) > (other.currency, other.amount)

    def __lt__(self, other):
        return (self.currency, self.amount) < (other.currency, other.amount)

    def __g3__(self, other):
        return (self.currency, self.amount) >= (other.currency, other.amount)

    def __le__(self, other):
        return (self.currency, self.amount) <= (other.currency, other.amount)

    def __repr__(self):
        return repr((self.currency, self.amount))

amount1 = Money('EUR', 10)
amount2 = Money('EUR', 20)
amount3 = Money('EUR', 10)

print(amount1 == amount2)
print(amount1 == amount3)
print(amount1 != amount2)

print(amount1 > amount2)
print(amount2 > amount3)

print(amount1 <= amount3)
print(amount1 >= amount3)
print(amount2 >= amount1)

from functools import total_ordering # all <, >=, <= are derived from __eq__ and __gt__
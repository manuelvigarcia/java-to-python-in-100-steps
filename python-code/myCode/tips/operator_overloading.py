class Money:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __add__(self, other):
        return Money(self.currency, self.amount + other.amount)

    def __sub__(self, other):
        return Money(self.currency, self.amount - other.amount)

    def __repr__(self):
        return repr((self.currency, self.amount))

amount1 = Money('EUR', 10)
amount2 = Money('EUR', 20)
print(amount1 + amount2)

print(amount2 - amount1)

class CurrenciesDoNotMatchException(Exception):
    def __init__(self, message):
        super().__init__(message)

class Amount:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
    def add(self, that):
        if(self.currency==that.currency):
            self.amount += that.amount
        else:
            raise CurrenciesDoNotMatchException(self.currency + ' and ' + that.currency + ' do not match.')

    def __repr__(self):
        return repr((self.currency, self.amount))

amount1 = Amount('EUR', 35)
amount2 = Amount('EUR', 50)
amount3 = Amount('INR',70)
print(amount1)
print(amount2)
print(amount3)

amount2.add(amount1)
print(amount1)
print(amount2)
print(amount3)

amount2.add(amount3)
print(amount1)
print(amount2)
print(amount3)

try:
    i=0
    number = 10/i
except ZeroDivisionError as error:
    print(error)
    number = 0
else:
    print('else')
finally:
    print("finally")

print(number)

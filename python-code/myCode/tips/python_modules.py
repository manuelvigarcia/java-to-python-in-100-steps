from decimal import Decimal

print (4.5 - 3.2) #prints 1.29999999999

value1 = Decimal('4.5')
value2 = Decimal('3.2')

print(value1 - value2) #prints 1.3

#built in float point is not accurate. Better to use Decimal. Specially for financial.

import math

print(math.pi)
print(math.e)
help(math.ceil) #documentation built in the modules

print(math.ceil(5.5))
print(math.ceil(-5.5))

import statistics
marks = [1,6,9,23,2]
print(statistics.mean(marks))
print(statistics.median(marks))
marks.append(7)
print(statistics.median(marks))

from collections import deque

queue = deque(['Zero', 'One', 'Two'])
print(queue)
queue.append('Three')
print(queue)
print(queue.pop())
print(queue)
queue.append('Three')
queue.append('Four')
queue.append('Five')
print(queue)
queue.appendleft('Minus One')
print(queue)
print(queue.popleft())
print(queue)

import datetime
today_date = datetime.datetime.today()
print(today_date)
print(today_date.year)
print(today_date.month)
print(today_date.day)
print(today_date.hour)
print(today_date.minute)

somedate = datetime.datetime(2025,5,25)
print(somedate)
print(somedate.date())
print(somedate.time())


print(somedate + datetime.timedelta(days=90))
print(somedate + datetime.timedelta(weeks=5))
print(somedate + datetime.timedelta(hours=72))
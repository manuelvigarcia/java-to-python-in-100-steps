from functools import reduce
numbers = [3,7,8,15,24,35,46]
months=[('Jan',31),('Feb',28),('Mar',31)]
#calculate the sum of the squares of the even numbers in the list
result = reduce(lambda x,y:x+y,map(lambda x:x**2, filter(lambda x:x%2==0, numbers)))
print(result)

#sum of the number of days of every month in the list
result = reduce(lambda x,y: x+y ,map(lambda x:x[1], months))
print(result)
#name of the month with the least number of days
result = reduce(lambda x,y:x if x[1]<y[1] else y, months)[0]
print(result)
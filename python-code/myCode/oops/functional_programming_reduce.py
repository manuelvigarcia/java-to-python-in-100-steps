from functools import reduce
numbers = [3,15,12,10]
words = ['Ant', 'Apple', 'Bat']
print(f'the sum of all numbers in the list is {sum(numbers)}')
print(f'the maximum of all numbers in the list is {max(numbers)}')
#sum of all numbers in the list
sum = reduce(lambda x,y:x+y, numbers)
print(sum)
#product of all numbers in the list
product_of_numbers = reduce(lambda x,y:x*y, numbers)
print(product_of_numbers)
#max of all numbers in the list
max_of_numbers = reduce(lambda x,y:max(x,y), numbers)
print(max_of_numbers)
#nin of all numbers in the list
min_of_numbers = reduce(lambda x,y:min(x,y), numbers)
print(min_of_numbers)

#Longest word
longest_word = reduce(lambda x,y: x if len(x)> len(y) else y, words)
print(longest_word)

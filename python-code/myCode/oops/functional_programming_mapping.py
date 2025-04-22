words=['Apple','Ant','Bat']
numbers=[1,5,2,9]
#all words in caps
all_caps_words = list(map(lambda x:x.upper(), words))
print(all_caps_words)
#lenght of each string
lengths_of_the_words = list(map(lambda x:len(x), words))
print(lengths_of_the_words)

#Squares of the numbers
squares=list(map(lambda x:x**2,numbers))
print(squares)
#squares of the first 10 numbers
squares_of_first_ten_numbers=list(map(lambda x:x**2, range(1,11)))
print(squares_of_first_ten_numbers)
#cubes of the first 10 numbers
cubes_of_first_ten_numbers = list(map(lambda x:x**3, range(1,11)))
print(cubes_of_first_ten_numbers)


numbers = [1, 89, 54, 35]
even_numbers = list(filter(lambda x: x%2==0, numbers))
odd_numbers = list(filter(lambda x:x%2, numbers))
print(even_numbers)
print(odd_numbers)

words = ['Apple', 'Ant', 'Bat', 'Frog', 'Cat']
#words ended in 'at'
at_ended_words = list(filter(lambda x:x.endswith('at'), words))
print(at_ended_words)
#words with length = 3
three_lengthed_words = list(filter(lambda x:len(x)==3, words))
print(three_lengthed_words)
#words starting with 'A'
words_started_in_A = list(filter(lambda x:x.startswith('A'), words))
print(words_started_in_A)
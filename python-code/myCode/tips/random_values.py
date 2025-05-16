import random
print(random.random())
print(random.random())
print(random.random())
print(random.random())

print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))

print(random.randrange(0,101, 5))
print(random.randrange(0,101, 5))
print(random.randrange(0,101, 5))
print(random.randrange(0,101, 5))
print(random.randrange(0,101, 5))


values = [2, 7,9,34,56]
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))

import string
print(random.choice(string.ascii_lowercase))
print(random.choice(string.ascii_lowercase))
print(random.choice(string.ascii_lowercase))
print(random.choice(string.ascii_lowercase))
letters = string.ascii_lowercase
print(random.sample(letters, 7))
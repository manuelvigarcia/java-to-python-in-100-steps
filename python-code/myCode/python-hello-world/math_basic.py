def print_squares_of_numbers_up_to(end_number):
    for i in range(1,end_number+1):
        print(i*i)

def print_squares_of_even_numbers_up_to(end_number):
    for i in range(2,end_number+1,2):
        print(i*i)

def sum_of_two_numbers(first, second):
    print(f"{first} + {second} = {first + second}")
    return first + second

def print_numbers_in_reverse(from_number):
    for i in range(from_number, 0, -1):
        print(i)

print_squares_of_numbers_up_to(3)
print_squares_of_even_numbers_up_to(6)
print_numbers_in_reverse(5)
print(sum_of_two_numbers(7,6))
print(sum_of_two_numbers(6,7))
print(sum_of_two_numbers(13,15))

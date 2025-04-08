for j in range(1,10):
    print(j)
print("done")

for j in range (1,10): print(j*j)

print("done")

def is_prime(number):
    if number < 2:
        print("Besides 1 and 2, only positive integers greater than three can be prime.")
        return False
    if number>2 and not number%2:
        print("Besides 2, only odd numbers can be prime.")
        return False
    for i in range (3, number//2, 2):
        if not number%i:
            print(f"{number} is multiple of {i}, so it is not a prime.")
            return False

    return True


def sum_up_to_number(number):
    total = 0
    for i in range(1, number+1):
        total = total + i

    return total


def sum_of_divisors(number):
    total = 0
    for i in range(2, number):
        if not number%i:
            total = total + i

    return total


def print_number_triangle(number):
    for i in range (1, number + 1):
        for k in range(1, i + 1):
            print(k, end=' ')

        print()


for j in range(1, 51):
    print(f"Sum of numbers from 1 to {j}: {sum_up_to_number(j)}")
    if is_prime(j):
        print(f"{j} is prime.")
    else:
        print(f"Sum of all divisors of {j}: {sum_of_divisors(j)}")

    print_number_triangle(j)

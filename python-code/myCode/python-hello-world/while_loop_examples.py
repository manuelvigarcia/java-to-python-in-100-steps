i = 0

while i < 11:
    print(i, end=' ')
    i += 1

print()

# all square numbers that are below a parameter
def squares_below_param(number):
    units = 1;
    while units * units  < number:
        print (units*units, end=' ')
        units = units + 1

    print()


# java do while with python while
def cube_of_input():
    number = 0
    while number >= 0:
        number = int(input("Enter a number: "))
        print(f"Cube of {number} is {number ** 3}")

    print("Thank you! Have Fun!")

squares_below_param(100)
cube_of_input()
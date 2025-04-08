def perform_operation_using_nested_if_else(number1=1, number2=1, operation=1):
    if operation == 1:
        print(f"Result: {number1} + {number2} = {number1 + number2}")
    elif operation == 2:
        print(f"Result: {number1} - {number2} = {number1 - number2}")
    elif operation == 3:
        print(f"Result: {number1} : {number2} = {number1 / number2}")
    elif operation == 4:
        print(f"Result: {number1} x {number2} = {number1 * number2}")
    else:
        print("Invalid operation.")


number_string = input("Enter Number1 ")
number1 = int(number_string)
number_string = input("Enter Number2 ")
number2 = int(number_string)

print("Available choices are:")
print("1 - addition")
print("2 - subtraction")
print("3 - division")
print("4 - multiplication")
op_string = input("Enter your choice ")
operation = int(op_string)

print(f"you decided to use {number1} and {number2} in a {operation} operation")

perform_operation_using_nested_if_else(number1, number2, operation)


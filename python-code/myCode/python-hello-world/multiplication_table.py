#print("Hello world")
from operator import concat


def print_hello_world_twice():
    print("Hello world 1")
    print("Hello world 2")


def print_hello_world_multiple_times(times):
    #print(times)
    for i in range(0,times):
        print("Hello world")


print_hello_world_multiple_times(4)


def print_table_from_to(table=5, fra=1, til=10):
    for i in range(fra, til + 1):
        print(f"{table} x {i} = {table*i}")

print_table_from_to()
print_table_from_to(6)
print_table_from_to(5, 3, 7)
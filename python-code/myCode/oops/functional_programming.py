def multiply_by_2(data):
    return data*2

def do_this_and_print(func, data):
    print(func(data))

do_this_and_print(multiply_by_2, 125)

func_example_reference = multiply_by_2

print(func_example_reference(23))

do_this_and_print(func_example_reference, 125)

#lambda:  lambda data:f(data)
#e.g.     lambda data:data*data
print('Lambda examples')
#multiply by 2
do_this_and_print(multiply_by_2, 2)
#multiply by 3
do_this_and_print(lambda data:data*3, 2)
#multiply by 5
do_this_and_print(lambda data:data*5, 2)
#calculate square
do_this_and_print(lambda data:data**2, 2)
#calculate cube
do_this_and_print(lambda data:data ** 3, 2)
#length of the string
do_this_and_print(lambda data:len(data), "this is a test")
#maximum of a list or set
do_this_and_print(lambda data:max(data), [123, 47, 1230, 21, 12, 3])
do_this_and_print(lambda data:max(data), {5,21,37,12,9})
#index of the maximum
do_this_and_print(lambda data:data.index(max(data)), [123, 47, 1230, 21, 12, 3])
#construct a set of the first n numbers
do_this_and_print(lambda n:set(i*i for i in range(1,n+1)), 7)
#Sum of the first n numbers
do_this_and_print(lambda n:sum(set(i for i in range(1,n+1))), 5)

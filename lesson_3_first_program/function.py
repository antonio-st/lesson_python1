# declare a function, we take 2 numbers as input - a and b
def multiply(a,b):
    print('a=', a)
    print('b=', b)
    result = a * b
    return result

def print_multiplay():
    print('Multiply 2 numbers: ')

# call the function
c = multiply(3,5)
print_multiplay()
print('c=', c, '\n')

c = multiply(400,5)
print_multiplay()
print('c=', c, '\n')

c = multiply(3,500)
print_multiplay()
print('c=', c, '\n')


# Write a function mult that accepts either one or two ints as arguments. If called with two arguments, the function prints the product of the two arguments. If called with one argument, it prints that argument.

def multiply(integer1, integer2=None):
    if integer2 is None:
        print(integer1)
    else:
        result = integer1 * integer2
        print(f'{integer1} * {integer2} = {result}')

multiply(3, 4)
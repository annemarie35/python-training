def test_primality():
    x = int(input('Enter an integer greater than 2: '))
    largest_divisor = None
    if x % 2 == 0:
        largest_divisor = int(x/2)
    else:
        for guess in range(3, x, 2):
            if x % guess == 0:
                largest_divisor = guess
                break
    if largest_divisor is not None:
        print('Largest divisor', 'of', x, 'is', largest_divisor)
    else:
        print(x, 'is a prime number')


test_primality()

def find_exponents():
    x = int(input('Enter an integer: '))
    exponents = 0
    for power in range(1, 7):
        for num in range(1, x+1):
            root = num
            if root**power == x:
                print(x, 'is the result of', root, '**', power)
                exponents += 1
    if exponents == 0:
        print('Number', x, 'has no exponents')
find_exponents()
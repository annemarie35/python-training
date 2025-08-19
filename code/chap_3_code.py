def find_cube_root():
    x = int(input('Enter an integer: '))
    answer = 0
    while answer**3 < abs(x):
        answer = answer + 1
    if answer**3 != abs(x):
        print(x, 'is not a perfect cube')
    else:
        if x < 0:
            answer = -answer
        print('Cube root of', x, 'is', answer)

find_cube_root()

def test_primality_smallest_divisor():
    x = int(input('Enter an integer greater than 2: '))
    smallest_divisor = None
    # First test that is an even number so no need to exhaustive iteration after that, even are divisible by 2
    if x % 2 == 0:
        smallest_divisor = 2
    else:
        for guess in range(3, x, 2):
            if x % guess == 0:
                smallest_divisor = guess
                break
    if smallest_divisor != None:
        print('Smallest divisor', 'of', x, 'is', smallest_divisor)
    else:
        print(x, 'is a prime number')
        
test_primality_smallest_divisor()

def find_square_root(x):
    epsilon = 0.01
    step = epsilon**2
    number_guesses = 0
    answer = 0
    while abs(answer**2 - x) >= epsilon and answer*answer <= x:
        answer += step
        number_guesses += 1
    print('Number of guesses=', number_guesses)
    if abs(answer**2 - x) >= epsilon:
        print('Failed to find a square root of ', x)
    else:
        print(answer, 'is close to the square root of ', x)

find_square_root(123456)

def find_square_root_bisection(x):
    epsilon = 0.01
    number_guesses, low = 0, 0
    high = max(1, x)
    answer = (high + low)/2

    while abs(answer**2 - x) >= epsilon:
        print('low=', low, 'high=', high, 'answer=', answer)
        number_guesses += 1
        if answer**2 < x:
            low = answer
        else:
            high = answer
        answer = (high + low)/2
    print('Number of guesses=', number_guesses)
    print(answer, ' is close to the square root of ', x)

find_square_root_bisection(23)
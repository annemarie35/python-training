# Ex 1 : What would the code if x = -25 in find_square_root_bisection function ?
# Answer : infinite loop with low= 0 high= 0.0 answer= 0.0, some are floats now

def find_cube_root_bisection(x):
    epsilon = 0.01
    number_guesses, low = 0, 0
    high = max(1, x)
    if x < 0:
        low = x
        high = 0
    answer = (high + low)/2

    while abs(answer ** 3 - x) >= epsilon:
        number_guesses += 1
        if answer ** 3 < x:
            low = answer
        else:
            high = answer
        answer = (high + low) / 2
    print('Number of guesses=', number_guesses)
    print(answer, ' is close to the cube root of ', x)

find_cube_root_bisection(-25)

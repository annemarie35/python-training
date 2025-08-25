def find_cubic_root_bisection(x):
    epsilon = 0.01
    number_guesses, low = 0, 0
    high = max(1, x)
    answer = (high + low) / 2

    while abs(answer ** 3 - x) >= epsilon:
        print('low=', low, 'high=', high, 'answer=', answer)
        number_guesses += 1
        if answer ** 3 < x:
            low = answer
        else:
            high = answer
        answer = (high + low) / 2
    print('Number of guesses=', number_guesses)
    print(answer, ' is close to the cubic root of ', x)

find_cubic_root_bisection(99)
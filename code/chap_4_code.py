def find_root(x, power, epsilon):
    # Find interval containing answer
    if x < 0 and power%2 == 0:
        return None #Negative number as no even-powered roots
    low = min(-1, x)
    high = max(1, x)

    # Use bisection search
    answer = (high + low) / 2
    while abs(answer**power - x) >= epsilon:
        if answer**power < x:
            low = answer
        else:
            high = answer
        answer = (high + low) / 2
    return answer

find_root(0.25, 1, 0.1)

def test_find_root(x_vals, powers, epsilons):
    for x_val in x_vals:
        for power in powers:
            for epsilon in epsilons:
                result = find_root(x_val, power, epsilon)
                if result is None:
                    val = 'No root exists'
                else:
                    val = 'Okay'
                    if abs(result**power - x_val) > epsilon:
                        val = ('Bad')
                print(f'x = {x_val}, power = {power}, epsilon = {epsilon}: val = {val}')

x_vals = [0.25, 8, -8]
powers = (1, 2, 3)
epsilons = (0.1, 0.001, 1)

test_find_root(x_vals, powers, epsilons)
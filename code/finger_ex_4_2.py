# Write a function mult that accepts either one or two ints as arguments. If called with two arguments, the function prints the product of the two arguments. If called with one argument, it prints that argument.
def multiply(integer1, integer2=None):
    if integer2 is None:
        print(integer1)
    else:
        result = integer1 * integer2
        print(f'{integer1} * {integer2} = {result}')

multiply(3, 4)

# Finger exercise: Using the algorithm of Figure 3-6, write a function that satisfies the specification
def find_log_base(x, base, epsilon):
    lower_bound = 0
    """Assumes x and epsilon int or float, base an int, x > 1, epsilon > 0 & power >= 1
    Returns float y such that base**y is within epsilon of x.
    """
    if x <= 1 or epsilon <= 0:
        return None

    while base**lower_bound < x:
        lower_bound += 1

    low = lower_bound - 1
    high = lower_bound + 1

    # Perform bisection search
    answer = (high + low) / 2
    while abs(base**answer - x) >= epsilon:
        if base**answer < x:
            low = answer
        else:
            high = answer
        answer = (high + low) / 2
    return answer

find_log_base(125, 3, 0.001)
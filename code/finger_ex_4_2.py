# Finger exercise: Using the algorithm of Figure 3-6, write a function that satisfies the specification
def find_log_base(x, base, epsilon):
    """Assumes x and epsilon int or float, base an int, x > 1, epsilon > 0 & power >= 1
    Returns float y such that base**y is within epsilon of x.
    """

    if x <= 1 or epsilon <= 0:
        return None

    lower_bound = 1 #power >= 1
    while base ** lower_bound < x:
        lower_bound += 1

    low = lower_bound -1
    high = lower_bound + 1

    answer = (high + low) / 2

    while abs(base**answer - x) >= epsilon:
        if base ** answer < x:
            low = answer
        else:
            high = answer
        answer = (high + low) / 2

    print(answer, 'is close to the log base', base, 'of', x)
    return answer


find_log_base(125, 3, 0.001)
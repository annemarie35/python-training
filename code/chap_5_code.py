def intersect(tuple1, tuple2):
    """Assumes t1 and t2 are tuples
    Returns a tuple containing elements that are in both t1 and t2
    """
    result = ()
    for e in tuple1:
        if e in tuple2:
            result += (e,)
    return result

print(intersect((1, 'a', 2), ('b', 2, 'a')))


def find_extreme_divisors(n1, n2):
    """
    Assumes that n1 and n2 are positive ints.
    Returns a tuple containing the smallest common divisor > 1 and the largest common divisor of n1 & n2.
    If no common divisor, other than 1, returns (None, None)
    """
    min_val, max_val = None, None
    for i in range(2, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            if min_val == None:
                min_val = i
            max_val = i
    return min_val, max_val

min_divisor, max_divisor = find_extreme_divisors(100, 200)
print(min_divisor)
print(max_divisor)
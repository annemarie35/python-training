# Write an expression that evaluates to the mean of a tuple of numbers. Use the function sum.

def evaluates_sum(numbers_tuple):
    length = len(numbers_tuple)
    numbers_sum = sum(numbers_tuple)
    return numbers_sum / length

print(evaluates_sum((1, 2, 3, 4, 5)))
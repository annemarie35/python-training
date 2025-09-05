# Finger exercise: Use the find_root function in Figure 4-3 to print the sum of approximations to the square root of 25, the cube root of -8, and the fourth root of 16. Use 0.001 as epsilon.
from chap_4_code import find_root

def print_sum_of_roots(square, cube, fourth, epsilon):
    square_root = find_root(square, 2, epsilon)
    cube_root = find_root(cube, 3, epsilon)
    fourth_root = find_root(fourth, 4, epsilon)
    return square_root + cube_root + fourth_root

print_sum_of_roots(25, -8, 16, 0.001 )

# Finger exercise: Write a function is_in that accepts two strings as arguments and returns True if either string occurs anywhere in the other, and False otherwise. Hint: you might want to use the built-in str operator in.
def is_in(text1, text2):
    return text1.lower() in text2.lower()

is_in('python', 'python')

# Finger exercise: Write a function to test is_in.
def test_is_in(words_list, word_to_check):
    for word in words_list:
        result = is_in(word, word_to_check)
        if result is True:
            print(f'{word} is in {word_to_check}')
        else:
            print(f'{word} is NOT in {word_to_check}')


words_list=['Python', 'p', 'python', 'a']
word='python'
test_is_in(words_list, word)

# Write a function mult that accepts either one or two ints as arguments. If called with two arguments, the function prints the product of the two arguments. If called with one argument, it prints that argument.
def multiply(integer1, integer2=None):
    if integer2 is None:
        print(integer1)
    else:
        result = integer1 * integer2
        print(f'{integer1} * {integer2} = {result}')

multiply(3, 4)
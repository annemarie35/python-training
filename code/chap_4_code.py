def find_root(x, power, epsilon):
    # Find interval containing answer
    # Below is docstring that will be displayed when using the built-in function help:
    """Assumes x and epsilon int or float, power an int, epsilon > 0 & power >= 1.
    Returns float y such that y**(power) is between epsilon of x.
    If such float does not exist, it returns None.
    """
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

def print_name(first_name, last_name, reverse):
    if reverse:
        print(last_name + ', ' + first_name)
    else:
        print(first_name, last_name)

print_name('Olga', 'Puchmajerova', False)
print_name('Olga', 'Puchmajerova', reverse = False)
print_name('Olga', last_name = 'Puchmajerova', reverse =False)
print_name(last_name = 'Puchmajerova', first_name = 'Olga', reverse = False)
# This raise a Syntax Error: print_name('Olga', last_name = 'Puchmajerova', False)

def mean(*args):
    # Assumes at least one argument and all arguments are numbers
    # Returns the mean of the arguments
    total = 0
    for arg in args:
        total += arg
    return total / len(args)


mean(1, 2, 3, 4)

def f(x): #name x used as formal parameter
    y = 1
    x = x + y
    print('x =', x)
    return x
x = 3
y = 2
z = f(x) #value of x used as actual parameter
print('z =', z)
print('x =', x)
print('y =', y)

def nested_scopes(x):
    # Figure 4-5 in book
    def func_g():
        x = 'abc'
        print('x =', x)
    def func_h():
        z = x
        print('z =', z)
    x = x + 1
    print('x =', x)
    func_h()
    func_g()
    print('x =', x)
    return func_g

x = 3
z = nested_scopes(x)
print('x =', x)
print('z =', z)
z()

# local variable 'x' referenced before assignment
def f():
    print('x in f =', x)

def g():
    # print('x in g =', x)
    x = 1

x = 3
f()
x = 67975765
g()
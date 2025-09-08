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

# Lists and mutability
L1 = [1, 2, 3]
L2 = L1[-1::-1] # Prints [3, 2, 1]
for index in range(len(L1)):
    print(L1[index]*L2[index])

Techs = ['MIT', 'Caltech'] #immutable
Ivys = ['Harvard', 'Yale', 'Brown'] #immutable
Univs = [Techs, Ivys]
Univs1 = [['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]
print('Univs =', Univs)
print('Univs1 =', Univs1)
print(Univs == Univs1) # Evaluates True but Univs and Univs1 are bound to quite different values.

Techs.append('RPI')
print('Univs =', Univs)
print('Univs1 =', Univs1)

L1 = [[]]*2 # creates a list with two elements, each of which is the same object
L2 = [[], []] # creates a list with two different objects
for index in range(len(L1)):
    L1[index].append(index)
    L2[index].append(index)
print('L1 =', L1, 'but', 'L2 =', L2)

L1 = [1,2,3]
L2 = [4,5,6]
L3 = L1 + L2
print('L3 =', L3)
L1.extend(L2)
print('L1 =', L1)
L1.append(L2)
print('L1 =', L1)

# Cloning

def remove_dups(L1, L2):
    """Assumes that L1 and L2 are lists.
    Removes any element from L1 that also occurs in L2"""
    for e1 in L1:
        print('L1', L1)
        print('e1 =', e1)
        if e1 in L2:
            L1.remove(e1)


L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dups(L1, L2)
print('L1 =', L1)


import copy
L = [2]
L1 = [L]
L2 = L1[:]
# L2 = copy.deepcopy(L1)
L.append(3)
print(f'L1 = {L1}, L2 = {L2}')

import copy
L1 = [2]
L2 = [[L1]]
L3 = copy.deepcopy(L2)
L1.append(3)
print('L1 =', L1) # Prints [2, 3]
print('L3 =', L3) # Prints [[[2]]]
print('L2 =', L2) # Prints [[[2, 3]]]

# An attempt to make copies all the way to the bottom would never terminate
L1 = [2]
L1.append(L1)
print('L1 =', L1)


import copy
L1 = [2]
L2 = [L1, L1] #
L3 = copy.deepcopy(L2)
L3[0].append(3)
print(L3)
print(L2)

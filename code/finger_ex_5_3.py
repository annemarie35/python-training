# What does the following code print?

L = [1, 2, 3]
L.append(L)
print(L is L[-1])
print(id(L[-1]))
print(id(L))
# Same ids

# Write a list comprehension that generates all non-primes between 2 and 100.

def all_non_primes():
    return [x for x in range(2, 101) if any(x % y == 0 for y in range(2, x))]

print(all_non_primes())
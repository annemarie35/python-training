# What does the following code print?

L = [1, 2, 3]
L.append(L)
print(L is L[-1])
print(id(L[-1]))
print(id(L))
# Same ids

# 5. Structured types and mutability


## Tuples

Tuples are immutable ordered sequences og elements (like strings),each can be of any type, not need to be all the same type.
Literals of type tuple are written by enclosing a comma- separated list of elements within parentheses.
For example:

```Python
t1 = ()
t2 = (1, 'two', 3)
t3 = (1) # will print 1
t4 = (1,)
```

- `print(t3)` is a verbose way to write the integer 1, to denote the singleton tuple containing this value, we write `(1,)`
- Repetition can be use `3 * ('a', 2)` evaluates to `('a', 2, 'a', 2, 'a', 2)`
- Like strings, tuples can be concatenated, indexed, and sliced.
- Tuples can contain tuples.

A `for` statement can be used to iterate over the elements of a tuple.
And the `in` operator can be used to test if a tuple contains a specific value.

### Multiple Assignment

If you know the length of a sequence (e.g., a tuple or a string), it can be convenient to use Python's `multiple assignment` statement to extract the individual elements.
For example `x, y = (3, 4)`

## Ranges and Iterables

### Ranges
The function `range` produces an object of type `range`, a sequence of integers.
Like strings and tuples, objects of type range are `immutable`.
All the operations on tuples (except concatenation and repetition) are available for ranges :
- for example `range(10)[2:6][2]`
- `==` operator cans compare objects of type `range`, it returns `True` if two ranges represent the same sequence of integers. 
  - For example, `range(0, 7, 2) == range(0, 8, 2)` evaluates to True
  - `range(0, 7, 2) == range(6, -1, -2)` evaluates to False because order is different

The most common use of `range` if in `for` loops. In Python 3, `range`is a special case of an `iterable oject`

### Iterables
All iterables types have a method `__iter__` that returns an object of `type iterator` that can then be used in a for loop to return a sequence of objects, one at a time.
Python has many built-in iterable types, including strings, lists, and dictionaries.

Many useful built-in functions operate on iterables, e.g. 
- `sum`: can be applied to an iterable of numbers
- `min`, `max` : to iterables for which there is a well-defined ordering on the elements (e.g. alphabetic list)

[finger exercice](/code/finger_ex_5_2.py)

## Lists and Mutability

### Lists
Like a tuple, a `list` is an ordered sequence of values, where each value is identified by an `index`. We use square brackets rather than parentheses.
- [] is an empty list
- [,] is a singleton
- lists are iterables, we can use a for statement to iterate over the elements of the list.
- we can also index into lists and slice

Using square brackets for three different purposes :
1. literals of type list,
2. indexing into iterables,
3. slicing iterables,
can lead to visual confusion, like `[1,2,3,4][1:3][1]`. In practice, most of the time lists are built incrementally rather than written as literals.

### Mutability
Lists are `mutable` ! In contrast, tuples and strings are `immutable`.

> Objects of immutable types cannot be modified after they are created. On the other hand, objects of mutable types can be modified after they are created.

The distinction between mutating an object and assigning an object to a variable may, at first, appear subtle, but remember the mantra: 
> “In Python a variable is merely a name, i.e., a label that can be attached to an object,”

![img.png](figure_5-2.png)

```python
Techs = ['MIT', 'Caltech'] #immutable
Ivys = ['Harvard', 'Yale', 'Brown'] #immutable
Univs = [Techs, Ivys]
Univs1 = [['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]
print('Univs =', Univs)
print('Univs1 =', Univs1)
print(Univs == Univs1) # Evaluates True but Univs and Univs1 are bound to quite different values. #test value equality

print(id(Univs) == id(Univs1)) #test object equality
print(Univs is Univs1) #test object equality
print('Id of Univs =', id(Univs))
print('Id of Univs1 =', id(Univs1))
```

Why the big fuss about the difference between value and object equality? It matters because lists are mutable.
If we change the list `Techs` with `Techs.append('RPI')`,the append method for lists has a `side effect`.
Rather than create a new list, it mutates the existing list, `Techs`, by adding a new element. 
Figure 5-3 depicts the state of the computation after `append` is executed.

![img.png](figure_5-3.png)

`Univs` list still contains two lists, but the content of `Techs` list has change now.

What we have here is called `aliasing`. There are two distinct paths to the same list object:
- via `Univs[0]` list which first element is bound to `Techs`
- via variable `Techs`

This can be convenient, but it can also be treacherous.

[finger exercice](/code/finger_ex_5_3.py)


The interaction of aliasing and mutability with default parameter values is something to watch out for
```python
def append_val(val, list_1 = []):
    list_1.append(val)
    print(list_1)
append_val(3)
append_val(4)
```
It will print `[3, 4]` and not `[4]` because:
- at function definition time, a new object of type list is created, with an initial value of the empty list.
- Each time `append_val` is invoked without supplying a value for the formal parameter `list_1`, the object created at function definition is bound to `list_1, mutated, and then printed

If we want to add the elements of one list into another list. We can do that by using list concatenation (using the + operator) or the `extend` method, e.g.

```python
L1 = [1,2,3]
L2 = [4,5,6]
L3 = L1 + L2
print('L3 =', L3) # Print [1, 2, 3, 4, 5, 6]
L1.extend(L2)
print('L1 =', L1) # Print [1, 2, 3, 4, 5, 6]
L1.append(L2)
print('L1 =', L1) # Print [1, 2, 3, 4, 5, 6, [4, 5, 6]]
```

Notice that the operator `+` does not have a side effect. It creates a new list and returns it. In contrast, `extend` and `append each mutate L1.

### Methods associated with lists
Note that all of these except `count` and `index mutate the list.

![img.png](figure_5-4.png)

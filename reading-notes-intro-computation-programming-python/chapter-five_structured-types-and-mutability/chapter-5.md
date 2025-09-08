# 5. Structured types and mutability


## Tuples

Tuples are immutable ordered sequences og elements (like strings),each can be of any type, not need to be all the same type.
Literals of type tuple are written by enclosing a comma- separated list of elements within parentheses.
For example:

```Python
t1 = ()
t2 = (1, ‘two', 3)
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
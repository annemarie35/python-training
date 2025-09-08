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
- Tuples can contain tuples

A `for` statement can be used to iterate over the elements of a tuple
And the `in` operator can be used to test if a tuple contains a specific value

### Multiple Assignment

If you know the length of a sequence (e.g., a tuple or a string), it can be convenient to use Python's `multiple assignment` statement to extract the individual elements.
For example `x, y = (3, 4)`
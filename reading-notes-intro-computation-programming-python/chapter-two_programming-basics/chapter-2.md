# Introduction to Python

//TODO Add vocabulary here

1990 by Guido Van Rossum
Python 2.0 in 2000
Python 3.0 in 2008


## Script, interpreter

A python `program`, sometimes called a `script`, is a sequence of `definitions` and `commands`.

A `command`, often called a `statement`, instructs the `interpreter` to do something.

When given a script, the Python interpreter will evaluate the definitions and executes the `commands`.

If the interpreter is launched from the shell and is given the script below, this will cause the message `Hello world!` to displayed on the shell standard output.
```python
print('Hello world!')
```

## Basics

### Objects

Objects are chore things manipulated by the program.

### Type

Objects have a type.

There are two type categories: 
- scalar (indivisible), e.g. the value `12`; 
- non-scalar (divisible), e.g. the string `Hello,world`, which can be split into `Hello,` and `world`. 

There are 4 scalars types : 
- `int` (standing for integer), eg `3` ;
- `float` (standing for floating-point number) , eg `3.0` ;
- `bool` (standing for boolean), which has two values : `True`, `False` ;
- `None`, which has one value : `Node`.

Scalar types are native to the language, you can't create a new scalar type. But you can create you own non-scalar type.

### Operators

Each type accept some operator.

The `int` and `float` types accepts these: 
* + : addition (plus)
* - : substraction (minus)
* * : multiplication/product (star)
* // : floor division  
* / : division (slash)
* % : remainder (percent)
* ** : power

The `bool` type accept these:
- and
- or
- not

### Expression

`Objects` and `operators` can be combined to form `expressions`.

The evaluation of an `expression` produce an `object`, called the `value` of an expression.

```python
3 + 2
```

In the expression above:
- `3` and `2` are `objects` of type int;
- `+` is a `operator`;
- `3 + 2` is an `expression`;
- the `value` of this `expression` is object `5`.

The `==` (double equal) operator is a special operator: it tests if two expressions evaluate to the same value.
It returns a boolean value.

```python
(3 + 2) == 5 
```

### Variables and assignments

`variables` provide a way to associate `names` with `object`.

The `=` (equal) operator : 
- associate a `name` to an `object`;
- define a `variable`, it is called a `definition`.

Here :
- the name `radius` is associated with the object whose value is 11
- the variable `radius` is defined.

```python
radius = 11
```

> In Python, a variable is just a name, nothing more. Remember this — it is important. An assignment statement associates the name to the left of the = symbol with the object denoted by the expression to the right of the = symbol. Remember this too: an object can have one, more than one, or no name associated with it

You can assign multiple values at once: it is called multiple assignment.
```python
x,y = 2, 3 
```

### mutability

An object can be mutable or immutable according to its type, e.g. `int` type are immutable.

Below, you don't change the value of object `1` to `2`.
You change the object assigned to the variable.
There are two objects, `1` and `2`, and object `1` has no name associated with it anymore at line 2.
```python
x = 1
x = 2
```

### literal and denotation

> Many objects can be denoted by literals in the text of a program.
> For example, the text 2 is a literal representing a number and the text abc is a literal representing a string.

The script below contains a line, with the text `2`.
```python
2
```

The interpreter will :
- identify this line as an expression;
- evaluate this expression to an object.

We'll say that :
- the literal `2`; 
- `denote` the object whose value is `2`.

This is tricky: 
- the `literal` is part of the program `source code`;
- the `object` is part of the program `execution`, stored in memory. 

## Control structures

### Branching programs

straight-line programs : computation that execute one statement after another in the order in which they appear
branching programs : simplest branching statement is conditional.
conditional statement has 3 parts:
- a test : an expression that evaluates to true or false
- a block of code executed if test evaluates to true
- an optional block of code executed if test evaluates to false

```python
if x%2 == 0:
    print('Even')
else:
    print('Odd')
print('Done with conditional')
```

== is used for comparison, since = is reserved for assignment
- Indentation is semantically meaningful in Python, and it is unusual used this way. It ensures that visual structure of a program is an accurate representation of its semantic structure
- long lines can be broken in multiple lines (if not it will be interpreted as two line and produces an 'unexpected indent error') with backslash (\) or ()

```python
x = (1111111111111111111111111111111 + 222222222222333222222222 +    
3333333333333333333333333333333)
```

if the true or false block contains another conditional statement, the conditional statements are said to be **nested**
elif in the above code stands for "else if"
It is often convenient to use a **compound Boolean expression** in the test of a conditional,example `if x < y and x < z:`


<---------------------------------------- TODO Read again this part ----------------------------------------------------->

## 2.4 Strings and input

'123' is a type string of 3 characters, not a number
operator + is **overloaded** with type strings, addition with 2 numbers but concatenation with strings
operator * is also overloaded, it is a repetition operator with strings : `3 * "a"` evaluates `aaa`
**type checking** : 'a'*'a' will throw an error

length : len(abc) -> 3
indexing : 'abc'[0] -> 'a'/ Error if out of range like 'abc'[10] / 'abc'[-1] -> 'c'
slicing : abc'[0:len('abc')] -> 'abc' / 'abc'[:] -> 'abc' (if values are omited around colon, defaults values are 0 and string length)
 
**Type conversions** or **type casts** :it is possible to convert objects of other type to string like `str(32)` -> `'32'`
int('3')*4 evaluates 12
with floats, the number is truncated and not rounded `int(4.665463)` -> `4`

the product of an int by a float is a float

**f-string** since Python 3.6
f or F following by a special kind od string literal called a **formatted string literal** : expressions bracketed by curly braces (double curly when having a curly inside)
`print(f'{25+25} is {1/2*100}% of {50*2}')` -> `50 is 50.0% of 100`

We can use modifiers in the expression inside a f-string adding a colon after `print(f'{3.14159:.2}')` -> 3.1 / `print(f'{15000000:,.0f}')` -> 15,000,000

### 2.4.1 Input
Input is a Python function to get input directly from user, takes a string as an argument displayed in the prompt `name = input('Enter your name: ')`
The line typed by the user is an object of type string and is returned by the function

```python
def birthday():
    birthday = input('Enter your birthday mm/dd/yyyy please: ')
    print(f'You were born in the year {birthday[6:10]}')
```

### 2.4.2 Disgression about character encoding
- ASCII standard for internal representation of characters, 128 were used for representing the usual set of english langague
- The **Unicode standard** is a character coding system designed to support the digital processing and display of the written texts of all languages. The standard contains more than 120,000 characters—covering 129 modern and historic scripts and multiple symbol sets. The Unicode standard can be implemented using different internal character encodings. You can tell Python which encoding to use by inserting a comment of the form

```
# -*- coding: encoding name -* 
for example :
# -*- coding: utf-8 -*-

```

instructs Python to use UTF-8, the most frequently used character encoding for webpages.18 If you don't have such a comment in your program, most Python implementations will default to UTF-8.
In 2016, 85% of websites were encoded using UTF-8

## 2.5 While loops
most computational tasks cannot be accomplished using branching programs
we use iteration when we want a program to do the same thing many times, a generic iteration also called a **looping**
begins with a **test** like a **conditional statement** 
- if the test evaluates to True, the program executes the **loop** body once then goes back to reevaluate the test
- the process is repeated until the test evaluates to False, after which control passes to the code following the iteration statement

we can use a **while** statement

**hand-simulating** the code using a pen and a paper or even a text editor

### finger exercice
[code](code/finger-ex-2-5.py)

## 2.6 For loop and range

iterating over a sequence, 'for variable in sequence'
```python
  total = 0
  for num in (77, 11, 3):
      total = total + num
  print(total)
```
The **variable** following for **is bound** to the first value in the sequence, and the code block is **executed**.
The expression (77, 11, 3) is a **tuple**, as a "sequence of value"

The built-in function **range** can generate a sequence of values, it will return a series of integers. It takes 3 int as argument with default values (can be negative) : start, stop and step.
```python
x= 4
for i in range(x):
print(i)
```
prints 0 1 2 3

the arguments of the range function are evaluated just before the first iteration loop
with nested loop, only the outer loop is concerned, the index of the inner loop will be reevaluated
see `nested_loops` in [code](/code/chap_2_code.py) 

### finger exercice
[code](code/finger-ex-2-6.py)

## 2.7 Style matters

> Just as style matters when writing in English, style matters when writing in Python. However, while having a distinctive voice might be an asset for a novelist, it is not an asset for a programmer. The less time readers of a program have to spend thinking about things irrelevant to the meaning of the code, the better.

Most Python programmers follow the conventions laid out in [PEP 8 style guide](https://peps.python.org/pep-0008/)
PEP is an acronym standing for “Python Enhancement Proposal.” PEP 8 was written in 2001 by Guido van Rossum, Barry Warsaw, and Nick Coghlan.

> if everyone uses the same set of conventions when writing Python, readers can concentrate on understanding the semantics of the code rather than wasting mental cycles assimilating stylistic decisions.

As stated in the famous [Zen of Python](https://peps.python.org/pep-0020/) in 1999
> Readability counts.

## 2.8 Terms Introduced in Chapter

- low-level language
- high-level language
- interpreted language
- compiled language
- source code
- machine code
- Python
- integrated development environment (IDE)
- Anaconda
- Spyder
- IPython console
- shell
- program (script)
- command (statement)
- object
- type
- scalar object
- non-scalar object
- literal
- floating point
- bool
- None
- operator
- expression
- value
- shell prompt
- variable
- binding
- assignment
- reserved word
- comment (in code)
- straight-line program
- branching program
- conditional
- indentation (in Python)
- nested statement
- compound expression
- constant time
- computational complexity
- conditional expression
- strings
- overloaded operator
- repetition operator
- type checking
- indexing
- slicing
- type conversion (casting)
- formatted string expression
- input
- Unicode
- iteration (looping) pseudocode
- while loop
- hand simulation
- break
- for loop
- tuple
- range
- in operator
- PEP 8 style guide
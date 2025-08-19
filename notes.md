# Notes

I start reading the book from [Introduction to Computer Science and Programming in Python MIT course](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/) by John B. Guttag, released in 2021

`Introduction to Computation and Programming Using Python, Third Edition
John V. Guttag;`

## Chapitre 1

> A computer does two things, and two things only: it performs calculations and it remembers the results of those calculations. But it does those two things very well.

Computationnel thinking 
Knowledge can be thought as either **declarative**(statement of facts) or **imperative** (how to knowledge or recipes)
Algorithm : a sequence of simple steps with a flow of control that specifies when to execute each steps. 

Early computers were fixed-program computers, exemple in 1941 Atanasoff and Berry or Turing's machine

//TODO Add vocabulary here

## Chapitre 2

//TODO Add vocabulary here

1990 by Guido Van Rossum
Python 2.0 in 2000
Python 3.0 in 2008

A python program, sometimes called a **script**, is a sequence of definitions and sequences.
The Python interpreter in the shell evaluates the definitions and executes the **commands**.
A command, often called a statement, instructs the interpreter to do something
```python
print('Hello world!')
```

Objects are chore things manipulated by Python, they have a type that can be scalar (indivisible) or non-scalar (for ex strings with internal structure)
literals can represent a number 2 or a string 'abc'

- 4 scalars types : int, float, bool, None

Objects and operators can be combined to form expressions. This is called the **value** of an expression.
Each expression evaluates to an object of some type. The expression below denotes the object 5.0 of type float
```python
3.0 + 2.0
```

operators on objects of type int and float are + - * // / % **
the primitive operators on type bool are and, or, and not»

### 2.2.2 Variables and assignements
variables provide a way to associate names with object
```python
radius = 11 #this is a comment
x,y = 2, 3 #multiple assignement
```
"In Python, a variable is just a name, nothing more. Remember this—it is important. An assignment statement associates the name to the left of the = symbol with the object denoted by the expression to the right of the = symbol. Remember this too: an object can have one, more than one, or no name associated with it"

### 2.3 Branching programs

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

### 2.4 Strings and input

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

### 2.4.5 While loops
most computational tasks cannot be accomplished using branching programs
we use iteration when we want a program to do the same thing many times, a generic iteration also called a **looping**
begins with a **test** like a **conditional statement** 
- if the test evaluates to True, the program executes the **loop** body once then goes back to reevaluate the test
- the process is repeated until the test evaluates to False, after which control passes to the code following the iteration statement

we can use a **while** statement

**hand-simulating** the code using a pen and a paper or even a text editor

```python
def while_loop():
    print_nb = input('How many times should i print the letter X?')
    to_print = 'x' * int(print_nb)
    print(to_print)
 
while_loop()
```

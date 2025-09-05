# Introduction to Python

//TODO Add vocabulary here

1990 by Guido Van Rossum
Python 2.0 in 2000
Python 3.0 in 2008


## Script, interpreter

A python `program`, sometimes called a `script`, is a sequence of `definitions` and `commands`.

A `command`, often called a `statement`, instructs the `interpreter` to do something.

When given a script, the Python interpreter will : 
- `evaluate` the `definitions`; 
- executes the `commands`.

If the interpreter is launched from the shell and is given the script below, this will cause the message `Hello world!` to displayed on the shell standard output.
```python
print('Hello world!')
```

// TODO: check that declaring a function is a definition 
// if so, and add a link to the chapter
// variable binding does not look like definition at all


## Statement, script

### One statement per line

If a `line` of the `script` file contains only one `statement`, it should not end with a special character.
If you can use the semicolon (`;`), the script will run, but Python programmers will be very surprised.
```python
print('Hello ')
print('world!');
```

### Several statements per line
If a `line` of the `script` file contains more than one `statement`, each statement should end with a semicolon, which act as a statement separator.
```python
print('Hello '); print('world!');
```

### One statement, several lines

Long lines can be broken in multiple lines, which means a statement can span several lines. 

To do so, end the line with backslash (`\`).
```python
x = 1 + \
3
print('he\
lo')
```

Do not put anything, even a space, after the backslash, or you'll get an error.
```python
x = 1 + \ 
3
```

You can sometimes use `implied line continuation`, a feature that know elements come in pair :
- if an opening element, say `(`, has not its closing pair `)` on the line; 
- it will read all lines till it finds it, say `)`; . 

Parentheses (`()`) are for expressions.
```python
x = (1 +     
2)
```

Brackets (`[]`) are for string. 
```python
text[1:
:3]
```

Braces/curly brackets (`{}`) are for dictionaries, as in Javascript.
```python
fruits = {
    "apple" : "red",
    "banana" : "yellow",
}
```

This may be surprising for you, as other languages like Java behave differently. 
[Source : Wikipedia](https://en.wikipedia.org/wiki/Semicolon#Programming)


## Objects, type, expression, variable

### Objects

Objects are chore things manipulated by the program.

This is an object
```python
2
```

Each object has a unique identifier.
To get it, pass the object in parameter of `id()` function.
```python
id(2) # 126275919282448
```

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

### Operator overloading

An operator is said to be overloaded because: 
- it has different meanings; 
- depending upon the types of objects to which it is applied.

An example is the plus (`+`) operator which means:
- on type number: addition, eg.  `1 + 2 == 3`;
- on type string: concatenation, eg. ` 'ab' + 'c' == 'abc' `.

### Expression, evaluation

`Objects` and `operators` can be combined to form `expressions`.

The `evaluation` of an `expression` produce an `object`, called the `value` of an expression.

```python
3 + 2
```

In the expression above:
- `3` and `2` are `objects` of type int;
- `+` is a `operator`;
- `3 + 2` is an `expression`;
- the `value` of this `expression` is object `5`.

### Equality

The `==` (double equal) operator is a special operator: it tests if two expressions (or objects) evaluate `to the same value`. It returns a boolean value.

```python
(3 + 2) == 5 # True 
```

The equality operator does not test if two objects are the same.
To do so, you should compare their identifiers.

```python
id('ab') == id('a' + 'b') # True
```

### Statement, expression

You may think that :
- all statements are expressions; 
- all expressions are statements.

> A command, often called a statement, instructs the interpreter to do something.
> Objects and operators can be combined to form expressions.

This is not so, as an expression should return an object.
> The evaluation of an expression produces an object, called the value of an expression.

So all statements that does not return values are not expression, as the statement below.
```python
print('Hello world!')
```

A statement can be an expression, but it is not very useful, as its value is lost.
```python
3 + 2
```

Statements usually use expressions.

They store their result in variables.
```python
result = 3 + 2
```

They use them to make tests.
```python
if (a + b == 3) :
    print('Hello')
```


### Variables, assignments, binding

`variables` provide a way to associate `names` with `object`, which is called `binding`.

The `=` (equal) operator : 
- associate a `name` to an `object`;
- bind an `object` to a `name`;
- define a `variable`, it is called a `definition`.

Here :
- the name `radius` is associated with the `object` whose value is 11;
- the variable `radius` is defined;
- `radius` is binded to `11`.

```python
radius = 11
```

> In Python, a variable is just a name, nothing more. Remember this — it is important. An assignment statement associates the name to the left of the = symbol with the object denoted by the expression to the right of the = symbol. Remember this too: an object can have one, more than one, or no name associated with it

You can assign multiple values at once: it is called multiple assignment.
```python
x,y = 2, 3 
```

> All of the expressions on the right-hand side of the assignment are evaluated before any bindings are changed.

```python
x, y = 1, 2
x , y = y, x
(x, y) == (2, 1) # True
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

### type conversion, coercion, casting

It is possible to convert objects: 
- from one type;
- to another type.

The conversion can be implicit, it is named `coercion`.
```python
2 * 1.0 == 2.0 # True
type(2 * 1.0) == float # True
```
When an operator combines two objects, it evaluates to the type which has a greater scale (here, float).

The conversion can be explicit, using a function named from the type, it is named `casting`.
```python
int('32') == 32    # True
float(32) == 32.0  # True
str(32) == '32'    # True
```

When converting from a type that has a greater scale than another one, some information is lost. 
E.g., when converting from`float` to `int`, the number is truncated to the integer part (not rounded).
```python
int(4.1) == 4 # true
```

[Wikipedia](https://en.wikipedia.org/wiki/Type_conversion) points out that :
- there are two conversion types :
   - the underlying data representation is `converted` from one representation into another, e.g. `int` to `float`, so precision may be lost;
   - a given representation is merely `reinterpreted` as the representation of another data type, e.g. `int` to `string`, so precision will not be lost;
- conversion is ruled by the typing paradigm :
    - strongly-typed languages do little `implicit conversion` and discourage `reinterpretation`;
    - weakly-typed languages do many `implicit conversions` and does not discourage `reinterpretation`.


### Type checking

Python has type checking, not as strong as strongly-typed language like Java. 
```python
'123' == 123         # False
```

Even if Python is weakly typed, it has stronger type checking than Javascript : the behaviour of `==` operator is different.
```js
'123' == 123   # true
'123' === 123  # false
```

Another example of type checking, for the repetition `*` operator.
```python
'hello' * 'world'
```

This operator expect an `int` as argument, so the expression below throws an error.

Python is dynamically typed, we'll see that in the [type-dedicated chapter](../chapter-for_typing).

### Literal and denotation

> Many objects can be denoted by literals in the text of a program.
> For example, the text 2 is a literal representing a number and the text abc is a literal representing a string.

The script below contains a line, with the text `2`.
```python
2
```

The interpreter will :
- identify this line as an `expression`;
- `evaluate` this `expression` to an `object`.

// TOOD: Check this, as an expression is expected to combine object and operator

We'll say that :
- the literal `2`; 
- `denote` the object (whose value is `2`).

This is tricky: 
- the `literal` is part of the program `source code`;
- the `object` is part of the program `execution`, stored in memory. 

If you run the program two times:
- the literal will stay the same;
- the object will not be the same.

## Text manipulation

### String type

Text (sequence of character) is stored in python in the string type, named `str`. There is no type for a single character. All string are immutable.

> There is no mutable string type
[Source](https://docs.python.org/3/library/stdtypes.html#str)

### Denotation

To `denote` text, quotes (simple or double) are used.
```python
type('123') == 'str' # True
type(123) == 'int'   # True
'123' == 123         # False
```

Do not get confused with Javascript :
- it is dynamically (weakly) typed, like python;
- but the behaviour of `==` operator is different.
```js
'123' == 123   # true
'123' === 123  # false
```

### Input

If you don't know the value of the text, you can't denote it. That happens if you want the user to supply the text, so yo can use `input` function.

It takes a string as an argument, for prompting
```python
name = input('Enter your name: ')
```

The function return text (`str` type), even if the user typed only number.

```python
def birthday():
    birthday = input('Enter your birthday mm/dd/yyyy please: ')
    print(f'You were born in the year {birthday[6:10]}')
```

### Operate on text

##### Length

The `len` function returns the length (character count) of a string. 

```python
len('abc') == 3 # True
```

##### Extracting

As the string is [non-scalar](#type) type, you can access its individual parts.

It is a `zero-based` array :
- text start at `index` 0;
- text end at index (length - 1).

To access a character, use the bracket operator `[index]`:
- if an index is out of range, you get an error;
- if the index is negative `[-n]`, you get the nth last character, which is (length - n) index.

```python
'abc'[0] == 'a'   # True
'abc'[3]          # IndexError: string index out of range
'abcd'[-2] == 'c' # True
'abc'[-3] == 'a'  # True
'abc'[-4]         # IndexError: string index out of range
```

To access a sequence of character, aka a substring, use the slice operator.
The slice operator is the bracket operator with two parameters : `[start:end]`.

The selection :
- begins at `start` index (lower bound), including; 
- stop at `end` index (upper bound), excluding - which may be surprising.

The matching mathematics interval is `[start:end[`.

```python
'abc'[1:2] == 'c'  # True
'abc'[1:3] == 'bc' # True
'abc'[0:len('abc')] == 'abc' # True
```

If values are omitted around colon, defaults values are : 
- start : 0;
- end : string length.

```python
'abc'[:] == 'abc' # True
``` 

// TODO: check what's happening, as it seems no copy is performed

This is a quick way to take a copy of the object
[Source](https://towardsdatascience.com/mastering-indexing-and-slicing-in-python-443e23457125/)

```python
id('abc') == id('abc'[:]) # False
```

#### Concatenating, combining

Use the `+` operator.
```python
'hello' + ' ' + 'world' == 'hello world' # True
```

The concatenation returns a new object. 
[Source](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)
> Concatenating immutable sequences always results in a new object. This means that building up a sequence by repeated concatenation will have a quadratic runtime cost in the total sequence length. To get a linear runtime cost, you must switch to one of the alternatives below

#### Generating text, repeating

You can generate text without using looping for simple usages. 

Use the repetition `*` operator.
```python
3 * 'abc ' == 'abc abc abc ' # True
```


#### Printing

**f-string** since Python 3.6
f or F following by a special kind od string literal called a `formatted string literal` : expressions bracketed by curly braces (double curly when having a curly inside)
`print(f'{25+25} is {1/2*100}% of {50*2}')` -> `50 is 50.0% of 100`

We can use modifiers in the expression inside a f-string adding a colon after `print(f'{3.14159:.2}')` -> 3.1 / `print(f'{15000000:,.0f}')` -> 15,000,000


### Character encoding

ASCII is the historical standard for internal representation of characters, which allow 128 characters. This was enough for representing the usual set of english language.

Unicode is a `standard` for character encoding system designed to support the digital processing and display of the written texts of all languages. The standard contains more than 120,000 characters—covering 129 modern and historic scripts and multiple symbol sets. 

The Unicode standard can be implemented using different internal character encodings. 
The most frequently used character encoding for webpages is UTF-8 (85% of websites in 2016).

You can tell Python which encoding to use to read teh file by inserting a special comment (UTF-8 is the default).
```
# -*- coding: $ENCODING_NAME -*- 
# -*- coding: utf-8 -*-
```

## Control flow

> control flow (or flow of control) is the order in which individual statements (...) of a program are executed
[Source : WP](https://en.wikipedia.org/wiki/Control_flow)

### Straight-line 

> Straight-line programs : they execute one statement after another, in the order in which they appear. The kind of computation we can describe are noty very interesting.

### Branching program

Note : The definition of branching program in the book seems limited to conditionals, as the author introduce the while loop implying it does not belong to branching program.
> Most computational tasks cannot be accomplished using branching programs (...). When we want a program to do the same thing many times, we can use iteration.   

But Wikipedia suggest branching include conditional and looping; we'll follow this way for headers.
> A branch is an instruction in a computer program that can cause a computer to begin executing a different instruction sequence and thus deviate from its default behavior of executing instructions in order.

> Branch instructions are used to implement control flow in program loops and conditionals (i.e., executing a particular sequence of instructions only if certain conditions are satisfied).  

[Source: WP](https://en.wikipedia.org/wiki/Branch_(computer_science)#cite_note-1)

#### Conditional

Conditional are not straight-line program because an instruction (or a group of) may not be executed.
There will be two path of execution if the script is executed two times, or with different input.
It is the classic if/then/else.

##### Conditional expression, if

The most simple need for conditionals is to assign a value or another to a variable.
```
if condition 
then variable = 'nominal'
else variable = 'alternative'
```

The reader has to check if the variable is the same if both branches.
That's what conditional expression are for : they enforce one single variable is assigned.  
```python
variable = if condition then 'nominal' else 'alternative'   
```

Conditional expressions are named expressions because [they are expressions](#expression-evaluation)  
> Many languages support conditional expressions, which are similar to if statements, but return a value as a result. Thus, they are true expressions (which evaluate to a value), not statements (which may not be permitted in the context of a value). 

[Source: WP](https://en.wikipedia.org/wiki/Conditional_(computer_programming)#If%E2%80%93then(%E2%80%93else))

> expr1 if condition else expr2
> If the condition evaluates to True, the value of the entire expression is expr1; otherwise it is expr2.

Let's see an example.
```python
mood = ( 'bad' if (name == 'garfield' and today=='monday') else 'good')
```

It is semantically equivalent to Javascript, in a different order.
```js
const mood = (name == 'garfield' && today=='monday') ? 'bad' : 'good'
```

We can see : 
- in Js, both alternatives are located together `'bad' : 'good'` ;
- in Python, one alternatives `bad` comes at the very beginning of the statement, and the other, `good` is at the very end. 

Python highlight one of the alternative, so choose the one which is most important.  

In other languages, conditional expression is implemented as an operator `? :`, eg. ` condition ? 'nominal' : 'alternative`, which is called ternary. In Python, you can't write conditional expression using an operator.
> In computer science, an operator is a ternary operator if it takes three arguments (or operands)
> Many programming languages feature the ternary conditional operator which defines a conditional expression that yields a value. This is sometimes referred to simply as the ternary operator, despite that several unrelated ternary operators exist. 
[Source: WP](https://en.wikipedia.org/wiki/Ternary_operation#Computer_Science)


##### Conditional statement, if

A conditional statement execute (or not) a block of code. 

A conditional statement has 3 parts :
- a test : a boolean `expression` - that evaluates to true or false, starting with `if` keyword and ending by a colon (`:`)
- a block of code, executed if the test evaluates to true - there is not `then` keywork
- a block of code, optional, executed if the test evaluates to false, starting with `else` keyword

```python
if x%2 == 0:
    print('Even')
else:
    print('Odd')
print('Done with conditional')
```

##### Test

The test can be any boolean expression.
```python
if sunHasSetInAndLightIsOn
if sunHasSetIn and LightIsOn
if x < y and x < z #compound Boolean expression
```

##### Code blocks

Blocks of code should be indented from the `if` to be valid.

Indentation is semantically meaningful in Python, which is unusual. 
It ensures that the visual structure of a program is an accurate representation of its semantic structure.

The code blocks can contain anything, including another conditional statement.
If so, it is said that conditional statements are `nested`.

##### Limitations

> Conditionals allow us to write programs that are more interesting than straight-line programs, but the class of branching programs is still quite limited. One way to think about the power of a class of programs is in terms of how long they can take to run. Assume that each line of code takes one unit of time to execute. If a straight-line program has n lines of code, it will take n units of time to run. What about a branching program with n lines of code ? It might take less than n units of time to run, but it cannot take more, since each line of code is executed at most once.

> A program for which the maximum running time is bounded by the length of the program is said to run in constant time. This does not mean that each time the program is run it executes the same number of steps. It means that there exists a constant, k, such that the program is guaranteed to take no more than k steps to run. This implies that the running time does not grow with the size of the input to the program.

> Constant-time programs are limited in what they can do. Consider writing a program to tally the votes in an election. It would be truly surprising if one could write a program that could do this in a time that was independent of the number of votes cast. In fact, it is impossible to do so. 

> The study of the intrinsic difficulty of problems is the topic of computational complexity. We will return to this topic several times in this book.
  Fortunately, we need only one more programming language construct, iteration, to allow us to write programs of arbitrary complexity.

#### Iteration, looping

##### While

most computational tasks cannot be accomplished using branching programs
we use iteration when we want a program to do the same thing many times, a generic iteration also called a **looping**
begins with a **test** like a **conditional statement** 
- if the test evaluates to True, the program executes the **loop** body once then goes back to reevaluate the test
- the process is repeated until the test evaluates to False, after which control passes to the code following the iteration statement

we can use a **while** statement

**hand-simulating** the code using a pen and a paper or even a text editor

[finger exercice](code/finger-ex-2-5.py)

##### For, range

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


[finger exercice](code/finger-ex-2-6.py)

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
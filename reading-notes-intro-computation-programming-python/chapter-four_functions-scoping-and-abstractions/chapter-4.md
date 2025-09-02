# 4. Functions, scoping, and abstraction

## Functions definitions

```python
def max_val(x, y):
      if x > y:
          return x
      else:
        return y
```

The PEP 8 convention is that function names should be in all lowercase with words separated by underscores to improve readability.

### Parameters or arguments
> The sequence of names within the parentheses following the function name (x,y in this example) are the **formal parameters** of the function.
> When the function is used, the formal parameters are bound (as in an assignment statement) to the **actual parameters** (often referred to as **arguments**) of the **function invocation** (also referred to as a **function call**).
> For example, the invocation binds x to 3 and y t o4.

> A function call is an expression, and like all **expressions**, it has a **value**. That value is returned by the **invoked** function.

Example:
```
def function(formal_parameter):
    # body of the function
    print(formal_parameter)
    
actual parameter = 'toto'

function(actual_parameter) # function invocation
```


**Lambda abstraction**
> The name “lambda abstraction” is derived from mathematics developed by Alonzo Church in the 1930s and 1940s. The name is derived from Church's use of the Greek letter lambda (λ) to denote function abstraction. During his lifetime, Church gave different explanations of why he chose the symbol lambda. My favorite is, “eeny, meeny, miny, moe".


### When a function is called:
1. **Expressions** that make up actual **parameters** are **evaluated** and formal parameters are **bound** to the resulting **values**
2. The **point of execution** (the next instruction to be executed) moves from the point of invocation to the first statement in the body of the function.
3. Code in the function's **body** is executed until a return **statement** is encountered
4. Value of the return is the **value** of function **invocation**
5. **Point of execution** is transferred back to the code following the **invocation**


## Keyword arguments and default value

There are two ways that formal parameters get bound :
- `positional` : eg. first formal parameter bound to first actual parameters, etc.
- `keyword arguments` : formal paramaters are bound using the name of the formal parameter

```python
def print_name(first_name, last_name, reverse):
    if reverse:
        print(last_name + ', ' + first_name)
    else:
        print(first_name, last_name)
```
Each of the following is an equivalent invocation of `print_name`:
- `print_name('Olga', 'Puchmajerova', False)`
- `print_name('Olga', 'Puchmajerova', reverse = False)`
- `print_name('Olga', last_name = 'Puchmajerova', reverse = False)`
- `print_name(last_name = 'Puchmajerova', first_name = 'Olga', reverse = False)`

> It is illegal to follow a keyword argument with a non-keyword argument aka positional. `print_name('Olga', last_name = 'Puchmajerova', False)` will raise a Syntax Error.

### Default parameters value

```python
def print_name(first_name, last_name, reverse=False):
    if reverse:
        print(last_name + ', ' + first_name)
    else:
        print(first_name, last_name)
```

Keyword arguments are commonly used in conjunction with `default parameter values`. 
It can help call a function with fewer arguments than specified. For example, `print_name('Olga', 'Puchmajerova')`

> using keyword arguments reduces the risk of unintentionally binding an actual parameter to the wrong formal parameter, which is a common blunder. It helps to reduce ambiguity in programmer's intentions.

## Variable number of arguments
Many Python's built-in functions (like `min` for example) operate with a variable number of arguments.
The `unpacking operator` allows a function to accept a variable number of positional arguments.
`*args` in the example below can be any more descriptive name.

```python
def mean(*args):
```

## Scoping
We have seen in chapter 2 that, in Python, a variable is just a name, nothing more.
Depending on the context, a variable can have the same name but will not be the same variable.
Each function defines a new `name space`, also called a `scope`.

What happens ?

1. At the top level, i.e., the level of the shell, a `symbol table` keeps track of all names defined at that level and their current bindings.
2. When a function is called, a new symbol table (often called a `stack frame`) is created. This table keeps track of all names defined within the function (including the formal parameters) and their current bindings. If a function is called from within the function body, yet another stack frame is created.
3. When the function completes, its stack frame goes away.

You can always determine the scope of a name by looking at the program text.
This is called `static` or `lexical scoping`.

### Stack and stack frame

```python
def nested_scopes(x):
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
```

x and z are variable outside of the function `nested_scopes` 
z evaluates the expression `nested_scopes(x)` by invoking the function `nested_scopes` with the value (3) to which x is bound 
When nested_scopes is entered, a `stack frame` is created,

When nested_scopes is entered, a stack frame is created containing:
- x, the formal parameter
- func_g
- func_h
The variables `func_g` and `func_h` are bound to objects of type function. The properties of these functions are given by the function definitions within `nested_scopes`.

#### When `func_h` is invoked from within `nested_scopes`
Yet **another stack frame is created.**
It adds z variable to stack but x (formal parameter of `nested_scopes`) is not contained. 
> A name is added to the scope associated with a function only if that name is
> - a **formal parameter** of the function
> - or a **variable bound** to an object within the body of the function

The appearance of a name (x in this case) that is not bound to an object anywhere in the function body (the body of func_h in this case) causes the interpreter to search the stack frame associated with the scope within which the function is defined (the stack frame associated with `nested_scopes`
- If the name is found (which it is in this case), the value to which it is bound (4) is used. 
- If it is not found there, an error message is produced: `Unresolved reference 'x'`.

When `func_h` returns, the stack frame associated with the invocation of `func_h` goes away, it is `popped` off the top of the stack

> Note that we never remove frames from the middle of the stack, but only the most recently added frame.
> Because of this **“last in first out”** (**LIFO**) behavior, we refer to it as a stack.
>
> Imagine cooking a stack of pancakes. When it comes time to eat the pancakes, the first pancake served will be the one on top of the stack.
![pancakes.png](pancakes.png)
> 
### When `func_g` is invoked from within `nested_scopes`

A stack frame containing `func_g`'s local variable x is added
When `func_g` returns, that frame is popped
When `nested_scopes` returns, the stack frame containing the names associated with `nested_scopes` is `popped`, getting us back to the original stack frame.

> Notice that when nested_scopes returns, even though the variable **func_g** no longer exists, **the object of type function** to which that name was once bound still exists.
> This is because functions are objects, and can be returned just like any other kind of object.
> So, **z** can be bound to the value returned by **nested_scopes**, and the function call **z()** can be used to _invoke the function that was bound to the name_ **func_g** within **nested_scopes** ,even though the name **func_g** is not known outside the context of **nested_scopes**.

### Order of references to a name

The order in which references to a name occur is not germane.
If an object is bound to a name anywhere in the function body (even if it occurs in an expression before it appears as the left-hand side of an
assignment), it is treated as local to that function.

```python
def f():
    print(x)
def g():
    print(x)
    x = 1
    
x = 3
f()
x = 3
g()
```

It prints 3 when f is invoked, but the error message `UnboundLocalError: local variable 'x' referenced before assignment`

> In fact, if your program depends upon some subtle scoping rule, you might consider rewriting to avoid doing so.

## Specifications

A `specification` of a function defines a `contract` between the implementer and the users of the function, aka its `clients`, with two parts:
- `assumptions`: describes conditions that must be met by the clients, typically constraints on actual parameters e.g. acceptable set of type and value (less frequent). For example, the specification of find_root might require that power be a positive integer.
- `guarantees`: describes conditions that must be met by the function, provided it has been called in a way that satisfies the assumptions. For example, the specification of find_root might guarantee that it returns None if asked to find a root that doesn't exist (e.g., the square root of a negative number).

Functions are a way of creating `computational elements` that we can think as `primitives` in two ways:

- `decomposition`: it creates structure. It allows us to **break a program into parts**
  - that are reasonably self-contained 
  - and that may be reused in different settings.
- `abstraction`: hides details. It allows us to use a piece of code as if it were a `black box`, that is, something whose interior details we
cannot see, don't need to see, and shouldn't even want to see. Abstraction is all about forgetting.
> That (abstraction) is the true art of programming. 

### Docstring & interactive help
The text between the triple quotation marks is called a `docstring` in Python.
By convention, Python programmers use docstrings to provide specifications of functions.
These docstrings can be accessed using the built-in function `help`, just typing in the IDE's python console:
```python
help(abs)
```

If you enter help(), an interactive help session is started, and the interpreter will present the prompt help> in the console window.
Type for example, `if` to display a description of the `if statement` 
Interactive help can be exited by entering quit.

## 4.3 Using functions to modularize code

## 4.4 Function as objects

## 4.5 Methods , oversimplified

## 4.6 Terms introduced in chapter

- function definition
- formal parameter
- actual parameter
- argument
- function invocation (function call)
- return statement
- point of execution
- lambda abstraction
- test function
- debugging
- positional argument
- keyword argument
- default parameter
- value unpacking operator (*)
- name space
- scope
- local variable
- symbol table
- stack frame
- static (lexical) scoping
- stack (LIFO)
- specification
- client
- assumption
- guarantee
- decomposition
- abstraction
- docstring
- help function
- first-class object
- higher-order programming
- lambda expression
- method
- dot notation


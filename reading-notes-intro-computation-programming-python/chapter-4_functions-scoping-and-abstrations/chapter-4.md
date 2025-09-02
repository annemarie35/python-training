# 4. Functions, scoping, and abstraction

```python
def max_val(x, y):
      if x > y:
          return x
      else:
        return y
```

The PEP 8 convention is that function names should be in all lowercase with words separated by underscores to improve readability.

> The sequence of names within the parentheses following the function name (x,y in this example) are the **formal parameters** of the function.
> When the function is used, the formal parameters are bound (as in an assignment statement) to the **actual parameters** (often referred to as **arguments**) of the **function invocation** (also referred to as a **function call**).
> For example, the invocation binds x to 3 and y t o4.

> A function call is an expression, and like all **expressions**, it has a **value**. That value is returned by the **invoked** function.

Lambda abstraction
> The name “lambda abstraction” is derived from mathematics developed by Alonzo Church in the 1930s and 1940s. The name is derived from Church's use of the Greek letter lambda (λ) to denote function abstraction. During his lifetime, Church gave different explanations of why he chose the symbol lambda. My favorite is, “eeny, meeny, miny, moe".


```
def function(formal_parameter):
    # body of the function
    print(formal_parameter)
    
actual parameter = 'toto'

function(actual_parameter) # function invocation
```

When a function is called:
1. Expressions that make up actual parameters are evaluated and formal parameters are bound to the resulting values
2. The **point of execution** (the next instruction to be executed) moves from the point of invocation to the first statement in the body of the function.
3. Code in the function's body is executed until a return statement is encountered
4. value of the return is the value of function invocation
5. Point of execution is transferred back to the code following the invocation

### 4.1.2 Keyword arguments and default value
missing parameters if not given -> throw an error
keyword arguments default values

### 4.1.3 Variable number of arguments
Many Python's built-in functions operate with a variable number of arguments
The **unpacking operator *** allows a function to accept a variable number of positional arguments.
```python
def mean(*args):
```

### 4.1.4 Scoping

## 4.2 Specifications

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


# 3. Some simple numerical programs

## 3.1 Exhaustive enumeration

**decrementing function** is a function that has the following properties:
- It maps a set of program variables into an integer. 
- When the loop is entered, its value is nonnegative.
- When its value is ≤ 0, the loop terminates.
- Its value is decreased every time through the loop.

See `find_cube_root` in [code](code/chap_3_code.py)
The algorithmic technique used in this program is a variant of **guess-and-check** called **exhaustive enumeration**.
> We enumerate all possibilities until we get to the right answer or exhaust the space of possibilities. At first blush, this may seem like an incredibly stupid way to solve a problem. Surprisingly, however, exhaustive enumeration algorithms are often the most practical way to solve a problem. They are typically easy to implement and easy to understand. And, in many cases, they run fast enough for all practical purposes.

Even if millions of guesses are required, run time is not usually a problem. Modern computers are amazingly fast
```python
    if x % 2 == 0:
        smallest_divisor = 2
```
See `test_primality_smallest_divisor` in [code](code/chap_3_code.py)

> The opportunity to trade code complexity for runtime efficiency is a common phenomenon. But faster does not always mean better. There is a lot to be said for simple code that is obviously correct and still fast enough to be useful.

## 3.2 Approximate solutions and bisection search

If a program prints the square root of a non-negative number, the result for 2 will be a non-rationnal value.
> there is no way to precisely represent its value as a finite string of digits (or as a float), so the problem as initially stated cannot be solved.
approximation
The thing this program can do is find an **** to the square root.

> Exhaustive enumeration is a search technique that works only if the set of values being searched includes the answer. In this case, we are enumerating the values between 0 and the value of x. When x is between 0 and 1, the square root of x does not lie in this interval. One way to fix this is to change the second operand of and in the first line of the while loop to get

See `find_square_root` in [code](code/chap_3_code.py)

<--------------------- TODO --------------->

We need to try another algorithm : bisection search.
Bisection search is an example of a **successive approximation** method.

> Such methods work by making a sequence of guesses with the property that each guess is closer to a correct answer than the previous guess. We will look at an important successive approximation algorithm, Newton's method, later in this chapter.

Like searching in a dictionnary, the words are in lexicographical order, this allows us to open the book to a page where we think the word might lie. We go backwards if the sequence of letters lexicographically precedes the first word on the page or forwards.
Take the same idea and apply it to the problem of finding the square root of x, we can exploit the fact that numbers are **totally ordered**.
Start searching in the middle then reduce the search space by only a small amount at each iteration.
At each iteration of the loop, the size of the space to be searched is cut in half. For this reason, the algorithm is called **bisection search**.

`find_square_root_bisection(123456789)` takes only 45 guesses


## 3.3 A Few Words about Using Floats

Floats are a good approximation to real numbers but only most of the time, can lead to surprising consequences.
`0.9999999999999999 is not 1.0`

Binary numbers
> A sequence of length n can represent 10n different numbers.


> using == to compare two floating-point values can produce a surprising result.
> It is almost always more appropriate to ask whether two floating point values are close enough to each other, not whether they are identical.
> So, for example, it is better to write abs(x‑y) < 0.0001 rather than x == y»

## 3.4 Newton–Raphson

## 3.5 Terms Introduced in Chapter

- decrementing
- function
- guess-and-check
- exhaustive enumeration
- approximation
- total ordering
- bisection search 
- successive approximation
- binary numbers
- bit
- switch
- floating point
- significant digits
- exponent
- precision
- rounding
- Newton–Raphson
- polynomial
- coefficient
- degree
- root
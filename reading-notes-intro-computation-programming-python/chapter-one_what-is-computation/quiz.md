# Quiz

## What is a computer ?

**What does `computer` mean ?
You can use Wikipedia to find out.**

> A machine that performs calculations and remembers the results of the calculations, very quickly. Those calculations are executed following a program, a finite sequence or list of instructions.

:bulb: Correction:
> I mean in a broader sense (history and etymology), not in the book's context.
>
> A computer is something or someone which is  `computing`.
>
> And `computing` is basically `calculating` (the simplest of all calculation being enumerating).
>
>The first entities called `computers` [were humans](https://en.wikipedia.org/wiki/Computer#Etymology). Basically, every human is a computer, a not-very efficient computer.
>
> `Computer` (someone that computer) comes from the latin verb [computo](https://en.wiktionary.org/wiki/compute) which means [calculate](https://en.wiktionary.org/wiki/calculate#English)
>> calculate, originally by means of pebbles
> 
>Calculus [are stones](https://en.wiktionary.org/wiki/calculus#Latin) which can be used for counting
>>From calcis, limestone, game counter s

**Find also a usage related to Easter.** 
> Something related to Blaise Pascal, so I would say the Pascaline, the first known calculator.

:bulb: Correction:
> Nope. AFAIK, Blaise Pascal was not involved with Easter.
>
> The answer was [computus](https://en.wikipedia.org/wiki/Date_of_Easter), which is an algorithm to find the date of easter.

**Is there such a thing as a human computer ?**
> Indeed, according to wikipedia and etymology of the word computer, since early-17th century the term is "_referred to a human computer, a person who carried out calculations or computations_".

**Why do we name computers "computers" ?**
> Because they perform calculation of mathematical or logical operations also called computations.

:bulb: Correction:
> As in [Wikipedia](https://en.wikipedia.org/wiki/Computer_(disambiguation)) disambiguation page, I wanted you to say we use "computer" when speaking about machine, because most of computer are nowadays machines.

**Is there a better name for them ?**
> I don't know, a computer performs calculations, and it remembers the result, so 'Calculator' could be used, but this word is more related to specific early computers and to desk calculators.

:bulb: Correction:
>A better name can be "automatic computer" or "machinic computer", whatever expression in which the non-human nature of operator stands out

**Does a computer use:**
**- declarative knowledge;** 
**- imperative knowledge ?**
> Imperative knowledge.

**What name did Alan Turing used to describe its machine ?**
> Universal Turing Machine.

:bulb: Correction:
> Nope. 
>
>According to [Wikipedia](https://en.wikipedia.org/wiki/Turing_machine), Turing did not have the pride of using its own name. He used a much more revealing name.
>> Alan Turing called it a "a-machine" (automatic machine)
>
>This name reveals the difference between a computer and [a automaton](https://en.wikipedia.org/wiki/Automaton)
>
>It was Alonzo Church who called it "Turing machine".

## Algorithm

**The cubic root is a function that :** 
**- given the volume of a cube (which has the same length side);**
**- return the side length.**

**Write down the previous sentence another way, eg. in declarative knowledge.**
> The cubic root of x is a number y such as y * y * y = x

**Write down an algorithm to find the cubic root of any positive number, if it exists.**
> See [code](code/quizz-chapter1-exercice.py)
 
**Then, write down its execution on input 99.**
> 4.62608528137207  is close to the cubic root of  99.

## Computer type

**Which type of computer is a desk calculator ?**
> A fixed-program computer, it can execute only one program
> [discussion online](https://www.quora.com/Are-calculators-considered-to-be-computers-If-not-then-why-do-they-have-similar-functions-to-computers)

:bulb: Correction:
> According to this [definition](https://en.wikipedia.org/wiki/Computer), is it still a computer ?
> 
>> A computer is a machine that can be programmed to automatically carry out sequences of arithmetic or logical operations (computation).
>
>What about [music boxes](https://en.wikipedia.org/wiki/Music_box) or [barrel organs](https://en.wikipedia.org/wiki/Barrel_organ) and other [automatons](https://en.wikipedia.org/wiki/Automaton)?

**Is the [Pascaline](https://en.wikipedia.org/wiki/Pascaline) a computer ? If not, why ?** 
> The Pascaline calculates and stores results so it could be considered as a computer in its larger definition, but the program cannot be changed so it cannot be considered as a computer.

:bulb: Correction:
> Well, the Pascaline is a desk calculator, so of desk calculator are computer, so do the Pascaline.

**In which computer architecture are data and programs stored in the same memory ?**
> A stored-program computer (not sure of this one).

:bulb: Correction:
> Nope, I was thinking about [Von Neuman](https://en.wikipedia.org/wiki/Von_Neumann_architecture) architecture

**On punched card, can you store data and programs ?**
> Yes, "cards were used for data input, storage, and software programming". [Source](https://en.wikipedia.org/wiki/Punched_card) 

## Language

In your square root algorithm, point down:
- a literal;
> 0.01
- an operator;
> /
- a variable.
> epsilon

Introduce a syntax error. Can the program be executed ? If so, does it return a valid answer ?
> No, the program crashes, and it returns an error 'SyntaxError: invalid syntax'.

Introduce a semantic error. Can the program be executed ? If so, does it return a valid answer ?
> Yes, it can, but the answer might be wrong or unexpected or never returned because of an infinite loop, for example.

## Executions

Guess some program execution [here](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/pages/in-class-questions-and-video-solutions/lecture-1/)
> Done !

## Compiler vs Interpreter

Write at least one programing language: 
- which is compiled;
> C++, Rust, C, Haskell, Go
- which is interpreted;
> Python, Ruby, Js, Php
- which is both.
> Python
concrete_math
=============

# Explorations into the methods and exercises of "Concrete Mathematics: A Foundation for Computer Science" by Graham, Knuth and Patashnik

## Chapter 1: Recurrent Problems

I've implemented the following algorithms in the first chapter:

* The solution to the "textbook" Josephus problem
* The solution to the binary generalization of the Josephus problem
* The solution generalized Josephus problem that can handle any cases
* A *naive* implementation of the REAL Josephus problem (where you skip every **TWO** warriors, instead of every other). I don't know a closed form solution.
* A small class util.zio that allows printing to a string instead of to STDOUT by enclosing in a context manager using `with`
* Code to convert a number to a sequence for a given radix and vice versa. This generalizes Python's `int()` constructor which can handle radixes of 2 through 36.

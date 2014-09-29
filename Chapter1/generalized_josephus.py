__author__ = 'zephaniahgrunschlag'

"""
Chapter 1 of "Concrete Mathematics" has a wonderful treatment of the Josephus
problem in great detail. The problem is generalized to the recurrence relation

f(j)     = alpha_j          for 1 <= j < d
f(d*n+j) = c*f(n) + beta_j  for 0 <= j < d and n >= 1

The most elegant approach solves the problem by viewing it a change of radix problem.
The solutions is given by:

f( (b_m b_m-1 b_m-2 ... b_2 b_1 b0)_d ) = (alpha_b_m beta_b_m-1 beta_b_m-2 ... beta_b_1 beta_b_0)_c

CAVEAT: Unfortunately, the ACTUAL historic Josephus problem is NOT covered by this generalized approach.
See historic_josephus.py for a brute force solution.
"""

class GeneralizedJosephusFactory:
    pass


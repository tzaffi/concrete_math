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

from Chapter1.radix import Radix

class GeneralizedJosephusFactory:

    def __init__(self, problem_type):
        self.problem_type = problem_type
        if self.problem_type not in ["standard", "binary", "general"]:
            raise ValueError("Unsupported Josephus solver of type", self.problem_type)

    def get_func(self, **kwargs):
        if self.problem_type == "general":
            err_msg = "Require radixes 'c' and 'd' and vectors 'alpha_vector' of length d-1 and 'beta_vector' of length d"
            try:
                self.c = kwargs["c"]
                self.d = kwargs["d"]
                self.alpha_vector = kwargs["alpha_vector"]
                self.beta_vector = kwargs["beta_vector"]
                if not isinstance(self.c, int) or not isinstance(self.d, int) or not \
                                len(self.alpha_vector) == self.d-1 or not len(self.beta_vector) == self.d:
                    raise ValueError(err_msg)
                return self.generalized_josephus
            except KeyError as ke:
                raise TypeError(err_msg, ke)

        elif self.problem_type == "binary":
            try:
                self.alpha = kwargs["alpha"]
                self.beta = kwargs["beta"]
                self.gamma = kwargs["gamma"]
                return self.binary_josephus
            except KeyError as ke:
                raise TypeError("Require parameters 'alpha', 'beta', and 'gamma':", ke)

        elif self.problem_type == "standard":
            return self.standard_josephus

    def generalized_josephus(self, x):
        # express x as a radix d number-sequence
        rad_d = Radix.tuple(x, base=self.d)

        # then apply the generalized josephus transformation to convert to a radix c number-sequence
        rad_c = [self.alpha_vector[rad_d[0]-1]]
        for dig in rad_d[1:]:
            rad_c.append(self.beta_vector[dig])

        # convert rad_c to a number and return
        return Radix.number(rad_c, base=self.c)

    def binary_josephus(self, x):
        # convert to a generalized Josephus problem by setting:
        # alpha_vector = (alpha,)
        # beta_vector = (beta, gamma)
        # c = d = 2
        self.alpha_vector = (self.alpha,)
        self.beta_vector = (self.beta, self.gamma)
        self.c = self.d = 2
        return self.generalized_josephus(x)

    def standard_josephus(self, x):
        # convert to a binary case by setting:
        # alpha = 1, beta = -1, gamma = 1
        self.alpha = self.gamma = 1
        self.beta = -1
        return self.binary_josephus(x)
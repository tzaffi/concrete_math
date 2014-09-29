__author__ = 'zephaniahgrunschlag'

from unittest.case import TestCase
from math import log2, floor

from Chapter1.generalized_josephus import GeneralizedJosephusFactory


class GeneralizedJosephusTest(TestCase):

    def setUp(self):
        self.josephus = GeneralizedJosephusFactory("standard")
        self.binary = GeneralizedJosephusFactory("binary")
        self.general = GeneralizedJosephusFactory("general")

    def test_initializers(self):
        #These are well defined:
        self.assertIsNotNone(self.josephus.get_func())
        self.assertIsNotNone(self.binary.get_func(alpha=1, beta=-1, gamma=1))
        self.assertIsNotNone(self.general.get_func(d=3, c=5, alpha_vector=(1, 2), beta_vector=(1,2,3)))

        #These aren't:
        self.assertRaises(TypeError, self.josephus.get_func, "any argument at all should raise")
        self.assertRaises(TypeError, self.binary.get_func)
        self.assertRaises(TypeError, self.binary.get_func, d=3)
        self.assertRaises(TypeError, self.binary.get_func, alpha=1, gamma=3)
        self.assertRaises(TypeError, self.general.get_func)
        self.assertRaises(TypeError, self.general.get_func, beta=3)
        self.assertRaises(TypeError, self.general.get_func, d=2, alpha_vector=(1, 2))
        self.assertRaises(TypeError, self.general.get_func, d=2, alpha_vector=(1, 2), alpha=5)
        self.assertRaises(TypeError, self.general.get_func, d=3, c=5, alpha_vector=5)
        self.assertRaises(TypeError, self.general.get_func, d=3, c=5, alpha_vector=(1, 2))
        self.assertRaises(ValueError, self.general.get_func, d=3, c=5, alpha_vector=(1, 2, 3), beta_vector=(1, 2, 3))

    def test_standard_josephus(self):
        j = self.josephus.get_func()
        self.assertEquals(j(1), 1)
        self.assertEquals(j(2), 1)
        self.assertEquals(j(3), 3)
        self.assertEquals(j(4), 1)
        self.assertEquals(j(5), 3)
        self.assertEquals(j(6), 5)
        self.assertEquals(j(7), 7)
        self.assertEquals(j(8), 1)
        for n in range(1, 101):
            self.assertEquals(j(2*n), 2*j(n)-1)
            self.assertEquals(j(2*n+1), 2*j(n)+1)

    def test_binary_josephus(self):
        j = self.josephus.get_func()

        #binary generalizes josephus:
        bj0 = self.binary.get_func(alpha=1, beta=-1, gamma=1)
        for n in range(1, 101):
            self.assertEquals(j(n), bj0(n))

        #special case: 2^m
        bj1 = self.binary.get_func(alpha=1, beta=0, gamma=0)
        mth_power = lambda x: 2 ** floor(log2(x))
        for n in range(1, 101):
            self.assertEquals(mth_power(n), bj1(n))

        #special case: constant == 1
        bj2 = self.binary.get_func(alpha=1, beta=-1, gamma=-1)
        for n in range(1, 101):
            self.assertEquals(1, bj2(n))

        #special case: linear function f(n) = n
        bj3 = self.binary.get_func(alpha=1, beta=0, gamma=1)
        for n in range(1, 101):
            self.assertEquals(n, bj3(n))

        #general case: f(n) = alpha*A(n) + beta*B(n) + gamma*C(n) where A(), B(), C() defined below:
        A = mth_power
        C = lambda x: x - A(x)
        B = lambda x: A(x) - C(x) - 1
        alpha, beta, gamma = 4, -2, 1
        f4 = lambda n: alpha * A(n) + beta * B(n) + gamma * C(n)
        bj4 = self.binary.get_func(alpha=alpha, beta=beta, gamma=gamma)
        for n in range(1, 101):
            self.assertEquals(f4(n), bj4(n))

        #recursive definition is satisfied:
        self.assertEquals(bj4(1), alpha)
        for n in range(1, 101):
            self.assertEquals(bj4(2*n), 2*bj4(n)+beta)
            self.assertEquals(bj4(2*n+1), 2*bj4(n)+gamma)

    def test_generalized_josephus(self):
        alpha_vect = (34, 5)
        beta_vect = (76, -2, 8)
        d = 3
        c = 10
        f = self.general.get_func(d=d, c=c, alpha_vector=alpha_vect, beta_vector=beta_vect)
        self.assertEquals(1258, f(19))

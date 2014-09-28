__author__ = 'zephaniahgrunschlag'

from unittest.case import TestCase

from generalized_josephus import GeneralizedJosephusFactory

class GeneralizedJosephusTest(TestCase):

    def setUp(self):
        self.josephus = GeneralizedJosephusFactory("standard")
        self.binary = GeneralizedJosephusFactory("binary")
        self.general = GeneralizedJosephusFactory("general")

    def test_initializers(self):
        #These are well defined:
        self.assertIsNotNone(self.josephus.get_func())
        self.assertIsNotNone(self.binary.get_func(alpha=1, beta=-1, gamma=1))
        self.assertIsNotNone(self.general.get_func(d=3, c=5, alpha_vector=(1, 2, 3)))

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
        for i in range(2,101):


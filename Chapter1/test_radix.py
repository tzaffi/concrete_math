__author__ = 'zephaniahgrunschlag'

from unittest.case import TestCase

from Chapter1.radix import Radix


class RadixTest(TestCase):

    def test_generalizes_python(self):
        s = "10010011110101001101011"
        for base in range(2, 33):
            self.assertEquals(int(s, base=base), Radix.number(s, base=base))
            self.assertSequenceEqual([int(c) for c in s], Radix.tuple(Radix.number(s, base=base), base=base))

    def test_handles_tuples(self):
        s = "10010011110101001101011"
        s_tuple = tuple(int(c) for c in s)
        for base in range(2, 33):
            self.assertEquals(Radix.number(s, base=base), Radix.number(s_tuple, base=base))
            self.assertEquals(s_tuple, Radix.tuple(Radix.number(s, base=base), base=base))

    def test_handles_arbitrary_expressions(self):
        t = (2.19, -3.14, 5.07, 203, 14)
        t_117 = (((2.19*117 -3.14)*117 +5.07)*117+203)*117 +14
        self.assertEquals(t_117, Radix.number(t, base=117))

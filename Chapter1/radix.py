__author__ = 'zephaniahgrunschlag'


class Radix:

    @staticmethod
    def number(x, base=10):
        """
        Use Horner's method to convert (x)_base to a number.
        :param x: an enumerable containing strings (such as a string)
        :type x:
        :param base:
        :type base:
        :return:
        :rtype:
        """
        if isinstance(x, str):
            x = [int(c, base=base) for c in x]
        y = 0
        for digit in x:
            y *= base
            y += digit
        return y

    @staticmethod
    def tuple(x, base=10):
        """
        Returns the radix sequence of the number x as a tuple. Any non-integral remainder is left in
        the least significant digit
        :param x:
        :type x:
        :param base:
        :type base:
        :return:
        :rtype:
        """
        if x < 0:
            raise ValueError("can only convert positive numbers to tuples of a given radix")
        if x == 0:
            return (0,)
        res = []
        while x > 0.0:
            x, d = divmod(x, base)
            res.append(d)
        return tuple(reversed(res))
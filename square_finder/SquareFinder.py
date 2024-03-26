import math
from itertools import permutations
from typing import Union


class SquareFinder:
    def __init__(self):
        pass

    @classmethod
    def find_square(cls, *args, checker=False) -> Union[tuple, int]:
        if len(args) == 1:
            return cls.square_circle(args[0])
        elif len(args) == 2:
            return cls.square_square(args)
        elif len(args) == 3:
            return cls.square_triangle(args, checker)
        raise Exception('not correct parameters')

    @classmethod
    def square_circle(cls, radius) -> int:
        return round(radius ** 2 * math.pi)

    @classmethod
    def square_square(cls, args) -> int:
        return args[0] * args[1]

    @classmethod
    def square_triangle(cls, args, checker) -> Union[tuple, int]:
        a, b, c = args
        p = (a + b + c) / 2
        pp = p * (p - a) * (p - b) * (p - c)
        if pp <= 0:
            raise Exception('No available triangle')
        if checker:
            for el in list(permutations(args)):
                if el[0] ** 2 == el[1] ** 2 + el[2] ** 2:
                    return round(math.sqrt(pp)), True
            return round(math.sqrt(pp)), False
        else:
            return round(math.sqrt(pp))

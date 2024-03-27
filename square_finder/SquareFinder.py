import math
from itertools import permutations
from typing import Union


class SquareFinder:
    def __init__(self):
        pass

    @classmethod
    def find_square(cls, *args: Union[int, float], checker=False) -> Union[tuple, float]:
        match len(args):
            case 1:
                return cls.square_circle(args[0])
            case 2:
                return cls.square_square(args)
            case 3:
                return cls.square_triangle(args, checker)
            case _:
                raise Exception('not correct parameters')

    @classmethod
    def square_circle(cls, radius) -> float:
        return round(radius ** 2 * math.pi, 2)

    @classmethod
    def square_square(cls, args) -> float:
        return round(args[0] * args[1], 2)

    @classmethod
    def square_triangle(cls, args, checker) -> Union[tuple, float]:
        a, b, c = args
        p = (a + b + c) / 2
        pp = p * (p - a) * (p - b) * (p - c)
        if pp <= 0:
            raise Exception('No available triangle')
        if checker:
            for el in [[a, b, c], [b, a, c], [c, a, b]]:
                if el[0] ** 2 == el[1] ** 2 + el[2] ** 2:
                    return round(math.sqrt(pp), 2), True
            return round(math.sqrt(pp), 2), False
        else:
            return round(math.sqrt(pp), 2)

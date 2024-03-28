import math
from abc import abstractmethod, ABC
from typing import Union


class Figure(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_area(self) -> Union[int, float]:
        return self.a * self.b


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_area(self) -> Union[int, float]:
        p = (self.a + self.b + self.c) / 2
        pp = p * (p - self.a) * (p - self.b) * (p - self.c)
        if pp <= 0:
            raise Exception('No available triangle')
        return round(math.sqrt(pp), 2)


class TriangleChecker(Triangle):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def check(self) -> bool:
        for el in [[self.a, self.b, self.c], [self.b, self.a, self.c], [self.c, self.a, self.b]]:
            if el[0] ** 2 == el[1] ** 2 + el[2] ** 2:
                return True
        return False


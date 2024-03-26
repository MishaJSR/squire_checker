from square_finder.SquareFinder import SquareFinder
from itertools import permutations


circle = SquareFinder.find_square(10)
triangle = SquareFinder.find_square(10, 10, 7)
triangle_checker = SquareFinder.find_square(3, 4, 5, checker=True)
squire = SquareFinder.find_square(10, 10)
print(circle)
print(triangle)
print(triangle_checker)
print(squire)

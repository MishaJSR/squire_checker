from square_finder.SquareFinder import SquareFinder

circle = SquareFinder.find_square(10)  # find squire of circle
triangle = SquareFinder.find_square(10, 10, 7)  # find squire of triangle
triangle_checker = SquareFinder.find_square(7, 24, 25, checker=True)  # find squire of triangle with checker of rectangle
squire = SquareFinder.find_square(10, 10) # find squire of squire
print(circle)
print(triangle)
print(triangle_checker)
print(squire)

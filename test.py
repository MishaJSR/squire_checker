from square_finder.SquareFinder import Rectangle, TriangleChecker, Triangle

rec = Rectangle(5, 3).calculate_area()
tri = Triangle(3, 4, 5).calculate_area()
right_tri = TriangleChecker(3, 5, 5).check()
right_tri_square = TriangleChecker(3, 4, 5).calculate_area()
print(rec)
print(tri)
print(right_tri)
print(right_tri_square)


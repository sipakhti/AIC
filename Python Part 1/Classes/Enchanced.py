class Text(str):
    def duplicate(self):
        return self + self


# Data Classes
from collections import namedtuple

# class Point:
#     def __init__(self, x , y):
#         self.x = x
#         self.y = y
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(p1 == p2)

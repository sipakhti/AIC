# Class: blueprint for creating new objects
# Object: instance of a class

# CREATING CLASS

# Classes are dynamic
class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def __str__(self):  # called when passing the object to the print method or using str()
        return f"({self.x}, {self.y})"

    # COMAPRISON MAGIC METHODS
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y

    # ARITHMETIC MAGIC METHODS
    def __add__(self, other):
        return Point(self.x + other.x,
                     self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x,
                     self.y - other.y)


# point = Point(1, 2)
# point.z = 10
# point.draw()
# zero_point = Point.zero()
# zero_point.draw()

# print(isinstance(point, object))

# COMPARING OBJECTS
point = Point(1, 2)
other = Point(1, 1)
print(point >= other)  # FALSE because both objects are at different memory locations



class HashTable:
    class Node:
        def __init__(self, key, value: int):
            self.key = key
            self.value = value

        @property
        def key(self):
            return self.__key

        @key.setter
        def key(self, key):
            self.__key = key

        @key.deleter
        def key(self):
            self.__key = None

        @property
        def value(self):
            return self.__value

        @value.setter
        def value(self, value):
            self.__value = value

        @value.deleter
        def value(self):
            self.__value = None

        def __eq__(self, other):
            if self.key == other.key:
                return self.value == other.value
            return False

        def __ge__(self, other):
            return self.value > other.value

        def __add__(self, other):
            return self.value + other.value

        def __sub__(self, other):
            return self.value - other.value

        def __mul__(self, other):
            return self.value * other.value

        def __mod__(self, other):
            return self.value % other.value

        def __truediv__(self, other):
            return self.value / other.value

        def __str__(self):
            return f"key: {self.key}, value: {self.value}"












node = HashTable.Node("a", 1)
print(node)

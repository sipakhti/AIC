# CUSTOM CONTAINER


class TagCloud:

    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


# PROPERTIES
class Product:
    def __init__(self, price):
        self.price = price  # unPythonic

    @property
    def price(self):
        return self.__price

    # if we donnot make a property setter then we can make it readonly
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value


product = Product(10)


# INHERITANCE


class Animal:

    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):

    # Method Override
    def __init__(self):
        super().__init__()
        self.weight = 2

    def walk(self):
        print("walk")


m = Mammal()
print(m.age)
print(m.weight)

# OBJECT CLASS
print(isinstance(m, object))
print(issubclass(Mammal, object))


# MULTIPLE INHERITENCE

class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person greet")


class Manager(Employee, Person):
    pass


manager = Manager()
manager.greet()

# A GOOD EXAMPLE OF INHERITENCE

class InvalidOperationError(Exception):
    pass

from abc import ABC, abstractmethod

class Stream(ABC):

    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

    @abstractmethod
    def read(self):
        pass

class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")

class MemoryStream(FileStream):
    def test(self):
        print("Reading data from memory stream")


# DUCK TYPING
# POLYMORPHISM

class UIControl(ABC):
    def draw(self):
        pass

class TextBox(UIControl):
    def draw(self):
        print("Text Box")

class DropDownList(UIControl):
    def draw(self):
        print("Drop Down List")

def draw(controls):
    for control in controls:
        control.draw()

ddl = DropDownList()
textbox = TextBox()


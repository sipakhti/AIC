# []
letters = ["a", "b", "c", "d"]

zeros = [0] * 5
combined = zeros + letters
numbers = list(range(20))
chars = list("Hello World")
print(len(chars))

# Accessing Items
letters = ["a", "b", "c", "d"]
print(letters[0])
print(
    letters[0:3])  # Slicing returns a new list containing elements within the range povided including the index itself

# LOOPING OVER LIST

letters = ["a", "b", "c", "d"]
for letter in letters:
    print(letter)
# we need the index as well then use enumerate which returns a tuple containing index and value
for (index, letter) in enumerate(letters):
    print(index, letter)

# ADDING OR REMOVING ITEMS
letters = ["a", "b", "c", "d"]

# Add
letters.append("e")  # At the end
letters.insert(0, "-")  # anywhere we want

# Remove
letters.pop()  # if no parameter is passed then pops the last element
letters.pop(0)  # if parameter is given then pops the element at the given index
letters.remove("b")  # removes the first occurrence of the given parameter
del letters[0:3]  # deletes a range of the elements
letters.clear()  # removes every element

# FINDING ITEMS
letters = ["a", "b", "c", "d"]
if "e" in letters:
    letters.index("e")
    # to prevent the method from raising an error
letters.index("a")  # return index of the parameter, if not found then the ValueError is raised
print(letters.count("f"))  # count occurrences of the the parameter

# SORTING LIST
numbers = [3, 51, 2, 8, 6]
# MODIFIES THE ORIGINAL LIST
numbers.sort()  # Ascending order
numbers.sort(reverse=True)  # Descending order
sorted(numbers)  # DOESNT MODIFY THE EXISTING LIST, RETURNS A NEW LIST

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

items.sort()
print(items)


def sort_item(item):
    return item[1]


# items.sort(key=sort_item)
# list.sort(key=lamda parameter:expression) -> expression is tbe value that is returned
items.sort(key=lambda item: item[1])  # Exactly the same as line 64
print(items)

# MAP FUNCTION
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]
# extract only prices -> old and ugly way
prices = []
for item in items:
    prices.append(item[1])

# same as the aboce for loop
# calls the lambda function on the passed iterable
map(lambda item: item[1],
    items)  # returns a map object, which is iterable thus list() function can be used to convert it into a list

# FILTER FUNCTION
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

# lambda parameter: boolean expression (if true returns the element and stores in the filter object)
x = list(filter(lambda item: item[1] >= 10, items))
print(x)

# LIST COMPREHENSION
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]
# basic syntax
prices = [item[1] for item in items]
print(prices)
filtered = [item for item in items if item[1] >= 10]
print(filtered)

# ZIP FUNCTION
list1 = [1, 2, 3]
list2 = [10, 20, 30]
print(list(zip("abc", list1, list2)))

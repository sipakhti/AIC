# Collection of key : value pair
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
print(point["x"])
point["z"] = 20
print(point)

# to make sure that error is not raised when a key is passed that doesnt exist
if "a" in point:
    print(point["a"])
# a much better way is to use the .get() method
print(point.get("a", 0))
del point["x"]  # to delete a key: value pair
print(point)

for key in point:  # simply loops over the keys of a dictionary
    print(key, point[key])

for key, value in point.items():  # dictionary.items() loops over tuples of (key, value)
    print(key, value)

# DICT COMPREHENSION
# {key: value for item in items}
values = {x: x * 2 for x in range(5)}







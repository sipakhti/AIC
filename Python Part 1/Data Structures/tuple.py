# Read only list

point = (tuple([1, 2]) + (3, 4)) * 3
print(point)
print(point[0])
print(point[0:2])
if 10 in point:
    print("exists")

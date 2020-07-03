numbers = [1, 2, 3, 1, 5, 6, 6]
first = set(numbers)
second = {1, 5}

union = first | second # UNION (items in the first or second set)
intersect = first & second # INTERSECTION (items in both first and second set)
difference = first - second # DIFFERENCE (items in left set but not in the right set)
symmetric = first ^ second # SYMMETRICAL DIFF (items that are not common)
print(union)


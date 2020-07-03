try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError) as ex:
    print("You didnt enter a valid age")
else:
    print("NO Exceptiojns were thrown")

# Raising exception in custom functions is costly



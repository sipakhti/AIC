# def greet(first_name, last_name=""):
#     print(f"Hi {first_name}")
#     print(f"Welcome aboard")
#
#
# greet("Umer", "Mehmood")
#
#
# # XARGS
# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total
#
#
# print(multiply(1, 2, 3, 4, 5))
#
#
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)
#
#
# print(factorial(5))


# # XXARGS
# # " ** " before an argument means that any parameter will be suplied as a key=value pair
# # and will be converted to a dictionary
#
# def save_user(**user):
#     print(user["funct"](6))
#
#
# save_user(id=1, name="Umer", age=22, funct=factorial)


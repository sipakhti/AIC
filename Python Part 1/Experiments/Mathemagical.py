
from decimal import Decimal
from math import sqrt


def rootextract(number, power=2):
    accuracy = 600
    square_array = calculate_denominator(number, power)
    if len(square_array) == 1:
        return square_array[0]

    denominator = square_array[0]
    square_root_of_denominator = square_array[1]

    denominator * (1 - ((denominator - number) / denominator))
    Q = Decimal((number - denominator) / denominator)
    exponent = Decimal(1 / power)

    partial_answer = Decimal(1 + (exponent * Q))

    for i in range(1, accuracy):
        partial_answer += (calculate_numerator(exponent, i) * Q ** (i + 1)) / factorial(i + 1)

    return partial_answer * square_root_of_denominator


def calculate_numerator(power, nth_term):
    if nth_term == 0:
        return power
    return Decimal(calculate_numerator(power, nth_term - 1) * (power - nth_term))


def factorial(n):
    if n == 1:
        return 1
    return Decimal(factorial(n - 1) * n)


def calculate_denominator(count, power):
    # for root in range(2, count):
    #     if root ** power == count:
    #         return [root]
    while True:
        count += 1
        # number = 2
        # while number < count:
        #     if number ** power == count:
        #         return [count, number]
        #     number += 1
        rang = (number for number in range(2, count))
        for number in rang:
            if number ** power == count:
                return [count, number]


user_in = " "
while True:
    try:
        user_in = int(input("Enter number: "))
        print(rootextract(user_in))
        print(sqrt(user_in))
    except ValueError:
        break

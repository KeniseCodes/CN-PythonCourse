'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

a, b = 10, 3.0
a_float = float(a)
b_int = int(b)
floor_division = a // b

value_1 = int(input("Please enter a number: "))
value_2 = int(input("Please enter another number: "))
multiply = value_2 * value_1

print(a_float, b_int, floor_division, multiply)

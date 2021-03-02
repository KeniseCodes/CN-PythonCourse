'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''
numbers = []
numbers_tuples = []
a = int(input("Please enter length of your list:"))
for x in range(a):
    numbers.append(int(input("Please enter a number to add to the list:")))
numbers.sort()
if a%2 != 0:
    numbers.append(0)
y = 0
while y < len(numbers):
    numbers_tuples.append(tuple(numbers[y:(y+2)]))
    y += 2
print(numbers_tuples)
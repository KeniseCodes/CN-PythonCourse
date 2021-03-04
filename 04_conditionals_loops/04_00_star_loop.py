'''

Write a loop that for a number n prints n rows of stars in a triangle shape.

For example if n is 3, you print:

*
**
***

'''

n = 5
x = 1
while x < n+1:
    print("*"*x)
    x += 1
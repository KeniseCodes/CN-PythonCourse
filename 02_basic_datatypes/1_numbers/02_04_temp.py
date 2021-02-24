'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"


'''

temp_f = int(input("Please enter a degree in Fahrenheit: "))
temp_c = (temp_f - 32) * (5 / 9)
print(temp_f, "degrees fahrenheit =", temp_c, "degrees celsius")

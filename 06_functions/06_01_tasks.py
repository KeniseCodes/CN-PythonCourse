'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean
def divisible_by_4_or_7(num):
    if num % 4 == 0 or num % 7 == 0:
        return True
    else:
        return False
# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean
def divisible_by_4_and_7(num):
    if num % 4 == 0 and num % 7 == 0:
        return True
    else:
        return False
# take in a number from the user between 1 and 1,000,000,000
user_number = int(input("Enter a number between 1 and 1,000,000,000:"))
# call your functions, passing in the user input as the arguments, and set their output equal to new variables 
result1 = divisible_by_4_or_7(user_number)
result2 = divisible_by_4_and_7(user_number)
# print your new variables to display the results
print(result1)
print(result2)
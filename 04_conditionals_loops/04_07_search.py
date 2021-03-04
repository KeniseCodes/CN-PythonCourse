'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''

n = int(input("Please enter a numer between 1 and 1,000,000,000:"))
i = 1
while i <= n:
    if i == n:
        print(n)
        break
    else:
        i += 1

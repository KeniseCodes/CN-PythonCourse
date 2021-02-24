'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''
script = input("Please enter a string: ").lower()
count = script.count("a") + script.count("e") + script.count("i") + script.count("o") + script.count("u")
print(count)


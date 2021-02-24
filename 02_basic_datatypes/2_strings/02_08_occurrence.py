'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''
script = input("Please enter a sentence: ")
letter = str(input("Please enter a letter: "))
result = script.index(letter)
print("String input:", script)
print("Letter input:", letter)
print("Result:", result)

'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

script = input("Please enter a string: ")
split_script = script.split(" ")
big = 0
word = ""
for x in split_script:
    if split_script.count(x) > big:
        big = split_script.count(x)
        word = x
print("The word with the most occurrences is:", word)
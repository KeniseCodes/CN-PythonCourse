'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''
strings = str(input("Please enter three words: "))
first_position = strings.index(" ")
last_position = strings.rindex(" ")
print(len(strings[0:first_position]), strings[0:first_position], sep=", ")
print(len(strings[first_position:last_position]), strings[first_position:last_position], sep=",")
print(len(strings[last_position:]), strings[last_position:], sep=",")
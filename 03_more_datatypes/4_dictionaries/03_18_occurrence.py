'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''
string = str(input("Please enter a string:"))
result = {}
for x in string:
    result.update({x:string.count(x)})
print(result)


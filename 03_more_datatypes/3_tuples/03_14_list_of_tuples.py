'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''
user_input = str(input("Please enter a string:"))
split_string = [user_input.split(" ")]
split_tuple = []
for s in split_string:
    for x in s:
        split_tuple.append(tuple(x))
print(split_tuple)

'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

script = input("Please enter a sentence: ")
symbol = input("Please enter a symbol: ")
first_char = script[0]
revised_script = script.replace(first_char, symbol)
print(revised_script)

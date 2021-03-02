'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''
list_in = []
for x in range(10):
    list_in.append(input("Please enter a number: "))
list_out = []
x = 1
while x < len(list_in):
    list_out.append(list_in[x])
    x += 2
list_in.reverse()
y = 1
while y < len(list_in):
    list_out.append(list_in[y])
    y += 2
print(list_out)


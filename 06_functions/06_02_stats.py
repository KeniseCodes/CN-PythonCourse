'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(data):
  # define the function here
  data.sort()
  lowest = example_list[0]
  highest = example_list[-1]
  sum = 0
  for num in data:
    sum += num
  avg = int(sum/len(data))
  print(f"The min is {lowest}")
  print(f"The max is {highest}")
  print(f"The average is {avg}")
  print(f"The sum is {sum}")


# call the function below here
stats(example_list)
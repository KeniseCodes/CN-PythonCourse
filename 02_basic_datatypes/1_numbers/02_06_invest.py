'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

inv_amount = int(input("Please enter investment anmount: "))
interest_rate = int(input("Please enter % interest rate: ")) / 100
years = int(input("Please enter number of years to invest: "))
future_value = inv_amount * ((1 + interest_rate) ** years)
print(future_value)
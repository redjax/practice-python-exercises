"""
Create a program that asks the user for a number and then prints out
a list of all the divisors of that number. (If you don’t know what a
divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""

number = int(input("Enter a number to all of its divisors: "))

list1 = list(range(1, number+1))
divisorList = []

for num in list1:
    if number % num == 0:
        divisorList.append(num)

print(divisorList)

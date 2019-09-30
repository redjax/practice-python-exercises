"""
Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?

Extras:

1. If the number is a multiple of 4, print out a different message.

2. Ask the user for two numbers: one number to check (call it num)
and one number to divide by (check). If check divides evenly into num,
tell that to the user. If not, print a different appropriate message.
"""

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("{} is even!".format(number))
elif number % 2 != 0:
    print("{} is odd!".format(number))
elif number % 4 == 0:
    print("Ooo, {} is a multiple of 4!".format(number))
else:
    print("Hmm...either that wasn't a number, or you broke me. Try again!")

"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that
they will turn 100 years old.

Extras:

1. Add on to the previous program by asking the user for another number
and printing out that many copies of the previous message.
(Hint: order of operations exists in Python)

2. Print out that many copies of the previous message on separate lines.
(Hint: the string "\n is the same as pressing the ENTER button)
"""
import datetime


def year_when_100():
    """Gets user's name & age, tells them
    what year they will be 100 years old.
    """
    # Get user input as variables for name & age
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    # How many years until user reaches age 100
    years_until_100 = 100 - age

    # Create variable for current year
    now = datetime.datetime.now()
    current_year = now.year

    # Add user's age to current year for age 100
    year_at_100 = current_year + years_until_100

    # Formatted message to display to user
    message = """
    ---\n
    Hello, {}.
    You are currently {} years old.
    The year right now is {}.
    You will be 100 years old in the year {}.
    """.format(name, age, current_year, year_at_100)

    print(message)


year_when_100()

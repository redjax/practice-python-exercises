"""
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of
the list that are less than 5.

Extras:

1. Instead of printing the elements one by one, make a new list that has
all the elements less than 5 from this list in it and print out this new list.

2. Write this in one line of Python.

3. Ask the user for a number and return a list that contains only elements
from the original list a that are smaller than that number given by the user.
"""


def print_lessthan_5(number):
    """Print number in list less than number."""
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list2 = []

    if number <= 10:
        for i in list1:
            if i < number:
                list2.append(i)
    else:
        print("Number must be between 1 and 10.\n")
        input("Press enter to try again...\n")
        print_lessthan_5(int(input("Enter a number between 1 and 10: ")))

    if number <= 10:
        print(list2)


print_lessthan_5(int(input("Enter a number between 1 and 10: ")))

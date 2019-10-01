"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only
the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

Extras:

1. Randomly generate two lists to test this
2. Write this in one line of Python (don’t worry if you can’t figure
this out at this point - we’ll get to it soon)
"""
import random

randList1 = list(range(1, random.randint(1, 50)))
randList2 = list(range(1, random.randint(1, 35)))

print_list = []

for num in randList1:
    if num in randList2:
        print_list.append(num)

print("Random List 1 Items: {}".format(randList1))
print("\nRandom List 2 Items: {}".format(randList2))
print("\n\nItems in both lists: ".format(print_list))

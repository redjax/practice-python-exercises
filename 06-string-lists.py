"""
Ask the user for a string and print out whether
this string is a palindrome or not.
(A palindrome is a string that reads the same
forwards and backwards.)
"""

test = [0, 1, 2, 3, 4, 5]

# print(test[::-1])

word_input = input("Enter a word, we'll tell you if it's a palindrome: ")


def reverse_word(word):
    reversed_word = word[::-1]
    return reversed_word


word_reversed = reverse_word(word_input)

if word_input == word_reversed:
    print("{} is a palindrome!".format(word_input))
else:
    print("{} is not a palindrome. Oh well!".format(word_input))

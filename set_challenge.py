# Create a program that takes some text and returns a list of all
# the characters in the text that are not vowels,
# sorted in alphabetical order.
#
# You can either enter the text from teh keyboard or
# initialise a string variable with the string.

vowels = frozenset('aeiou') #  frozen set is being used because the members mustn't change

while True:
    string_to_check = set(input("Enter a sentence to take out the vowels "))
    print("The sentence '{}' without vowels is ".format(string_to_check))
    print(sorted(string_to_check.difference(vowels)))
    repeat = input("Do you want to check another sentence? (y/n) ")
    if repeat == "n":
        break

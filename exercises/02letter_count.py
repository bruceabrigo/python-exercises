# Write a function called `letter_count` to count the letter
# occurrence in a string. Use a dictionary.

# u can iterate over a string one letter at a time using
# a for loop.
#
# for letter in "alpha":
#   print(letter)
#
# Create a dictionary with `dd = {}`. Assign values with `dd["foo"] = 1`.
# Check to see if a dictionary has a key using the `in` operator.
#
#
# Careful. Python requires that you insert a key into a dictionary
# before you try to modify it's value. If you try to access a dictionary
# at a key that hasn't been added you'll get an error and the program will
# crash. Remember to use an if statement to see if a key is "in" a dictionary
# before you try to read it!
#
# d2 = {}
# d2["foo"]
# > KeyError: 'foo'
#
# Example function call:
#
# letter_count('banana')
#
# > {'a': 3, 'b': 1, 'n': 2}

def letter_count(str):
    pass # takes input from str in function call
    Dict = {}
    pass # defines an empty dictionary to be assigned value
    pass # print each index for each letter in str
    for letter in str:
        if letter in Dict:
            pass # if the letter exists in Dict, add 1 to its value
            Dict[letter] += 1
        else:
            Dict[letter] = 1
    return Dict

Dict = letter_count('racecar')
pass # pass to <str> in letter_counter fun, which will be defined as an input for Dict
print(Dict)
# return the value of each counted letter in the str
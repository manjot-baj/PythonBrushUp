"""
Aim: Write a Function, function for check pangram
"""

import string


def ispangram(user_string):
    alphabet = string.ascii_lowercase
    return set(alphabet) <= set(user_string.lower())


print(ispangram("the quick brown fox jumps over the lazy dog"))

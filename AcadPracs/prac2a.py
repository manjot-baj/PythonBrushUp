"""
Aim: Write a Function, Vowel check
"""


def vowel_check(ch):
    vowels = ["a", "e", "i", "o", "u"]
    if ch.lower() in vowels:
        print(ch, "is a vowel.")
    else:
        print(ch, "is not a vowel.")


my_ch = input("Enter any char(A-Z/a-z) only:")
vowel_check(my_ch)

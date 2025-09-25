"""
Aim: Write a program, that accepts the user’s name and age as input,
 and displays the year in which the user will turn 100 years old.
"""

name = input("what is your name:")
age = int(input("how old are you:"))
year = str((2025 - age) + 100)
print(name + "you will b 100 years old in year" + year)

"""
Aim: Write a Function, Calculate Length of any datatype
"""


def calculate_length(n):
    count = 0
    for i in n:
        count = count + 1
    return count


print(calculate_length([1, 3, 5, 7, 9]))
print(calculate_length("Sonali"))

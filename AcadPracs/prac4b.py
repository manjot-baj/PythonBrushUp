"""
Write a program, Print the elements of the list with 
the condition applied with List comprehension
"""

name_list = ["yashu", "vedu", "somu", "pari", "sanu", "rudra", "mou"]
new_name_list = [
    list_element
    for (list_index, list_element) in enumerate(name_list)
    if list_index not in (0, 2, 4, 5)
]

print(new_name_list)

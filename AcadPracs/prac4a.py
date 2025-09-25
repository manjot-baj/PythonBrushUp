"""
Write a Function, Check if common in List by comparing the list elements.
"""


def check_if_common(list1, list2):
    response = False
    for x in list1:
        for y in list2:
            if x == y:
                response = True
    return response


print(check_if_common([4, 6, 8, 10, 12], [5, 7, 8, 10, 11]))
print(check_if_common([3, 5, 7, 9, 11], [2, 4, 6, 8]))

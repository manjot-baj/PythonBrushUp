"""Write a program to detect double space in a string"""

text= "There is a double space  here"

# if "  " in text:
#     print("Double space detected ")
# else:
#     print("No Double space detected ")

#method 2
index= text.find("  ")
if index != -1:
    print("Double space detected ")
else:
    print("No Double space detected ")
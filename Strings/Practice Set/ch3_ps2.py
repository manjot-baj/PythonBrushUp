"""
Write a program to fill in a letter template given below with name and date.
"""

name= input("enter your name:")
date= input("enter date:")
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
letter= letter.replace( "<|Name|>", name)
letter= letter.replace( "<|Date|>", date)
print(letter)
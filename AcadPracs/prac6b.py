"""
Program to Read and Write a File
"""

f = open("PythonBrushUp/AcadPracs/abc.txt", "a+")
f.write("\nblah\n")
f = open("PythonBrushUp/AcadPracs/abc.txt", "r")
t = f.read()
print(t)
f.close()

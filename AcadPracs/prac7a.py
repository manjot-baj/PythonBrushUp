"""
WAP Create a student info class
"""


class Student:
    def info(self, studname, studaddr):
        print("Name:", studname, "Address:", studaddr)


obj = Student()
obj.info("Veda", "Airoli")

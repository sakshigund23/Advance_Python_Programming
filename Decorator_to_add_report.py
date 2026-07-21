# Decorator to add a report header
def report_header(func):
    def wrapper(*args, **kwargs):
        print("=" * 40)
        print("         STUDENT REPORT")
        print("=" * 40)
        func(*args, **kwargs)
        print("=" * 40)
    return wrapper


class Report:
    college = "MIT ADT University"

    # Constructor (Magic Method)
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    # Class Method
    @classmethod
    def change_college(cls, new_name):
        cls.college = new_name

    # Magic Method
    def __str__(self):
        return f"Name : {self.name}\nRoll No : {self.roll}\nMarks : {self.marks}"

    # Decorator applied to display report
    @report_header
    def display_report(self):
        print(f"College : {Report.college}")
        print(self)
        if self.marks >= 40:
            print("Result : PASS")
        else:
            print("Result : FAIL")


# Main Program

student1 = Report("Shriram", 51, 91)
student1.display_report()
print()

Report.change_college("Pune Institute of Computer Technology")

student2 = Report("Karan", 222, 36)
student2.display_report()
'''Output:-
PS C:\Users\Shriram\Desktop\SY-Advance-Python> & C:\Users\Shriram\AppData\Local\Microsoft\WindowsApps\python3.13.exe c:/Users/Shriram/Desktop/SY-Advance-Python/Assignment_2.py
========================================
         STUDENT REPORT
========================================
College : MIT ADT University
Name : Shriram
Roll No : 51
Marks : 91
Result : PASS
========================================

========================================
         STUDENT REPORT
========================================
College : Pune Institute of Computer Technology
Name : Karan
Roll No : 222
Marks : 36
Result : FAIL
========================
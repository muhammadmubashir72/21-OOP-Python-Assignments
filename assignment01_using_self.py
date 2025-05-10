# ✅ 1. Using self
# Assignment: Create a class Student with attributes name and marks. Use the self keyword to initialize 
# these values via a constructor. Add a method display() that prints student details.

class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, \nMarks: {self.marks}")


student1 = student("Muhammad Mubashir Saeedi", 99)
student1.display() 

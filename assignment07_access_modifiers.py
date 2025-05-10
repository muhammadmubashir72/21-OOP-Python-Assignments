# ✅ 7. Access Modifiers: Public, Private, and Protected
# Assignment: Create a class Employee with:
# a public variable name,
# a protected variable _salary,
# a private variable __ssn.
# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")

# Creating an instance of the Employee class
employee1 = Employee("Mubashir", 50000, "123-45-6789")
employee1.display()

print(f"Accessing Public Variable: {employee1.name}")
print(f"Accessing Protected Variable: {employee1._salary}")

try:
    print(f"Accessing Private Variable: {employee1.__ssn}")
except AttributeError as e:
    print(f"Error: {e}")


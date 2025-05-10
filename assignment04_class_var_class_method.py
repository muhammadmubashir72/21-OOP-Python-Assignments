# ✅ 4. Class Variables and Class Methods
# Assignment: Create a class Bank with a class variable bank_name. 
# Add a class method change_bank_name(cls, name) that allows changing the bank name. 
# Show that it affects all instances.

class Bank:
    bank_name = "State Bank"  

    def __init__(self, customer_name):
        self.customer_name = customer_name

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name 

    def display(self):
        print(f"Customer: {self.customer_name}, Bank: {Bank.bank_name}")

customer1 = Bank("Muhammad Mubashir Saeedi") 
customer2 = Bank("Asad")

customer1.display()  
customer2.display()  

Bank.change_bank_name("HBL Bank")

customer1.display()  
customer2.display() 
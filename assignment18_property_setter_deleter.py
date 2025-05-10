# ✅ Question 18: Property Decorators: @property, @setter, and @deleter

# Assignment: Create a class Product with a private attribute _price. 
# Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    _price = 0
    def __init__(self, price):
        self._price = price
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self._price = new_price
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price
# Example usage
product = Product(100)
print(product.price)  
product.price = 150  
print(product.price)
del product.price
try:
    print(product.price)
except AttributeError as e:
    print(e)


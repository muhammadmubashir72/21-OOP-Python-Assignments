# ✅ Question 19: callable() and __call__()

# Assignment: Create a class Multiplier with an __init__() to set a factor. 
# Define a __call__() method that multiplies an input by the factor. 
# Test it with callable() and by calling the object like a function.
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor
# Example usage
multiplier = Multiplier(3)
print(multiplier.factor) 
 
print(callable(multiplier))
print(multiplier(5))  
print(multiplier(10))  
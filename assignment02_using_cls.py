# # ✅ 2. Using cls
# Assignment: Create a class Counter that keeps track of how many objects have been created. 
# Use a class variable and a class method with cls to manage and display the count.f

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"Number of objects created: {cls.count}")

counter1 = Counter()
counter2 = Counter()
counter3 = Counter()

Counter.display_count() 
class Dog:
    # init method allows us to instantiate the object when it is created.
    def __init__(self):
        pass
    
    def add_one(self, x):
        return x + 1
    
    def bark(self):
        print("bark")

# A method is essentially just a function inside a class.
# Creating an instance of the class Dog.
d = Dog()
d.bark()
print(type(d))

print(d.add_one(5))
# d is an object of the class Dog.

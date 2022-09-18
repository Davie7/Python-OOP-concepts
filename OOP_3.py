class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

d = Dog("Tim", 34)
print(d.get_name())
print(d.get_age())
d.set_age(23)
print(d.get_age())

d1 = Dog("Bill", 14)
print(d1.get_name())
print(d1.get_age())
d1.set_age(33)
print(d1.get_age())

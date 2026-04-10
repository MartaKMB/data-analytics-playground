class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

    def __str__(self):
        return f"{self.name} says: {self.speak()}"

class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    pass
    # def speak(self):
    #     return "Meow!"
    
class Cow(Animal):
    def speak(self):
        return "Moo!"
    
gecko = Animal("Staś")

dog = Dog("Burek")
cat = Cat("Mruczek")
cow = Cow("Mućka")

print(gecko)
print(dog)
print(cat)
print(cow)

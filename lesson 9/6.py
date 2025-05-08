class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):  # Dog يرث من Animal
    def bark(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):  # Cat يرث من Animal
    def meow(self):
        print(f"{self.name} says Meow!")

# استخدام الأصناف
dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.eat()  # Output: Buddy is eating
dog.bark() # Output: Buddy says Woof!

cat.eat()  # Output: Whiskers is eating
cat.meow() # Output: Whiskers says Meow!

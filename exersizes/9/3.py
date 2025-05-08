#  1. أنشئ صنف أساسي `Animal` يحتوي على:
#     - خاصية name
#     - دالة make_sound() تطبع "Some generic sound"

#  2. أنشئ صنفين يرثان من Animal:
#     - `Dog`: دالة make_sound()  تطبع "Woof!"
#     - `Cat`: دالة  make_sound() تطبع "Meow!"

#  3. أنشئ كائنين من كل صنف واستدعِ make_sound()  لكل منهما

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")
    
class Cat(Animal):
    def make_sound(self):
        print("Meow!")

dog = Dog("Buddy")
cat = Cat("Whiskers")
dog.make_sound()
cat.make_sound()
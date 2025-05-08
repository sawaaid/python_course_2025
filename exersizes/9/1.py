#  1. أنشئ صنف اسمه `Person` يحتوي على:
#     - خاصية الاسم (name)
#     - خاصية العمر (age)
#     - دالة `introduce()` تطبع "Hello, my name is [name] and I'm [age] years old."
#  2. أنشئ كائنين من هذا الصنف واستدعِ الدالة introduce() لكل منهما

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Hello, my name is %s and I'm %g years old."%(self.name, self.age))

p1=Person("Ali", 25)
p2=Person("Sari", 30)
p1.introduce()
p2.introduce()
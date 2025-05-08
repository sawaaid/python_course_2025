class Student:
    # المُنشئ (Constructor)
    def __init__(self, name, age):
        self.name = name  # خاصية
        self.age = age    # خاصية
    
    # وظيفة (Method)
    def study(self, subject):
        print(f"{self.name} is studying {subject}")


student1 = Student("Ahmed", 20)
student2 = Student("Fatima", 22)


student1.study("Math")  # Output: Ahmed is studying Math
student2.study("Physics")  # Output: Fatima is studying Physics

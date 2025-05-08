class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def increase(self):
        self.price += 10


product=Product("Laptop", 1200)
print(product.name,product.price)
product.increase()
print(product.name,product.price)

###########################
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Doctor(User):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization

d=Doctor("Dr. Smith", 35, "Cardiology")
print(d.name, d.age, d.specialization)
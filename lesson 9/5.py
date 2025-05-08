class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0  # قيمة افتراضية
    
    def accelerate(self):
        self.speed += 10
        
    def brake(self):
        self.speed -= 5

my_car = Car("Toyota", "Corolla", 2020)
print(my_car.speed)  # 0 (القيمة الافتراضية)
my_car.accelerate()
print(my_car.speed)  # 10

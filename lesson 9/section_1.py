# class Product:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#         print(f"{self.name} : {self.price}")
    
#     def increase(self):
#         self.price += 0.1
#         print(self.price)

# p = Product("iceCreame",0.2)
# p.increase()

class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Doctor(User):
    def __init__(self, specialization,name, id):
        super().__init__(name, id)
        self.specialization = specialization
    
    def show_info(self):
        print(f"Doctor Name: {self.name}, ID: {self.id}, Specialization: {self.specialization}")

class Hospital(User):
    def __init__(self, adress,name, id):
        super().__init__(name, id)
        self.adress = adress
    
    def show_info(self):
        print(f"Hospital User_ame: {self.name}, ID: {self.id}, adress: {self.adress}")



doctor = Doctor("fadi",1,"global")
doctor.show_info()
hospital = Hospital("tamer",2,"cairo")
hospital.show_info()
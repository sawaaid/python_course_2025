class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # خاصية خاصة
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid amount")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds")
    
    def get_balance(self):
        return self.__balance
# استخدام الصنف
account = BankAccount("Ali", 1000)
account.deposit(500)  # Output: Deposited 500. New balance: 1500
account.withdraw(200) # Output: Withdrew 200. New balance: 1300

# محاولة الوصول المباشر للرصيد
print(account.__balance)  # Error! لا يمكن الوصول مباشرة
print(account.get_balance())  # الطريقة الصحيحة: 1300

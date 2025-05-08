#  أنشئ صنف ` BankAccount` مع:
#  - خصائص خاصة: __account_number  و __balance
#  - المُنشئ يأخذ رقم الحساب والرصيد الأولي
#  - دالة  deposit(amount) تضيف المبلغ للرصيد
#  - دالة withdraw(amount)  تخصم المبلغ من الرصيد (إذا كان الرصيد كافي)
#  - دالة get_balance()  ترجع الرصيد الحالي
#  - دالة display_info()  تطبع رقم الحساب والرصيد

#  أنشئ كائن واختبر جميع الدوال مع مراعاة حماية البيانات

class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds or invalid withdrawal amount.")
            
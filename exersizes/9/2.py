#  أنشئ صنف `Book` يحتوي على:
#  - المُنشئ يأخذ عنوان الكتاب (title) والمؤلف (author) وعدد الصفحات (pages)
#  - دالة `display_info()` تعرض معلومات الكتاب
#  - دالة `is_thick()` ترجع True إذا كان عدد الصفحات أكثر من 300، وإلا False
#  
#  أنشئ كائنين من هذا الصنف واختبر الدوال


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def display_info(self):
        print("Title: %s, Author: %s, Pages: %g" %(self.title, self.author, self.pages))
    
    def is_thick(self):
        return self.pages > 300

b1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
b2 = Book("War and Peace", "Leo Tolstoy", 1225)
b1.display_info()
b2.display_info()
b1.is_thick()
b2.is_thick()
# y="syria is free"
"""
This script processes a text file containing city data and performs various operations on it.
Steps:
1. Opens a file named "lesson 5/4.txt" with UTF-8 encoding.
2. Reads all lines from the file and calculates the total number of lines.
3. Splits each line into words using tab ("\t") as a delimiter.
4. Extracts numerical data from the third column, removes commas, and converts it to integers.
5. Extracts city names from the first column.
6. Appends the numerical data to the `num` list and city names to the `cities` list.
7. Prints the list of cities and their corresponding numerical values.
8. Defines a predefined list of values representing data for specific cities.
9. Calculates the sum of the predefined values and prints the total.
Comments in Arabic:
- يقوم البرنامج بفتح ملف نصي يحتوي على بيانات المدن.
- يتم قراءة جميع الأسطر من الملف وحساب عدد الأسطر.
- يتم تقسيم كل سطر إلى كلمات باستخدام علامة التبويب ("\t") كفاصل.
- يتم استخراج البيانات الرقمية من العمود الثالث وتحويلها إلى أرقام صحيحة.
- يتم استخراج أسماء المدن من العمود الأول.
- يتم إضافة البيانات الرقمية إلى قائمة `num` وأسماء المدن إلى قائمة `cities`.
- يتم طباعة قائمة المدن والقيم الرقمية المقابلة لها.
- يتم تعريف قائمة مسبقة بالقيم التي تمثل بيانات لمدن محددة.
- يتم حساب مجموع القيم المسبقة وطباعة الإجمالي.
"""
# # u.append(m)
# # u.extend(m)
# # u.sort(reverse=True)
# # print(u)
# # y=u.pop(1)
# # del u[1:3]
# t=y.split()
# d=":"
# e=d.join(t)
# print(e)
# # num = int(input("number is:"))
# # print(num in u)

# # for item in u:
# #     print(item)

# # for i in range(len(u)):
# #     print(u[i])

# # أكتب برنامج يقوم بإدخال قيمة 
# # والبحث عنها في القائمة إن كانت أو لا

file = open("lesson 5/4.txt",encoding="utf-8")
lines=file.readlines()
print(len(lines))
num=[]
cities=[]
for line in lines:
    words=line.split("\t")
    m=words[2].replace("\n","")
    num.append(int(m.replace(",","")))
    cities.append(words[0])
print(cities)
print(num)

values = [
    1832,  # حلب
    1678,  # ريف دمشق
    1327,  # حمص
    1129,  # إدلب
    812,   # درعا
    622,   # حماة
    485,   # دير الزور
    429,   # دمشق
    176,   # الرقة
    128,   # المخيمات الفلسطينية
    38,    # اللاذقية
    35,    # طرطوس
    53,    # الحسكة
    20,    # القنيطرة
    3      # السويداء
]

# Calculate the sum
total = sum(values)

print("Total:", total)
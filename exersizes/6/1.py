names = ("salah","khalid","omar","qa3a3","ahmad")
print(names)


even = (2, 4, 6, 8)
odd = (1, 3, 5, 7)

combined = even + odd
print("Combined tuple:", combined)


students = (
    ("Omar", 85),
    ("Lina", 92),
    ("Khaled", 78)
)

for student in students:
    name, grade = student
    print(f"الطالب {name} حصل على علامة {grade}")

languages = ["python", "java", "dart"]
lang_tuple = tuple(languages)
print(lang_tuple)

employees=[
    ("omar","IT",25,200),
    ("jana","programmer",33,500),
    ("sa3id","engineer",44,700)

]
def add_emplyee():
    name=input("name:")
    age=int(input("age"))
    salary=float(input("salary"))
    department=input("department")
    employees.append((name,department,age,salary))

def search_employee():
    search_name=input("name")
    for name,department,age,salary in employees:
        if search_name==name:
            print(name,age,department,salary)
        

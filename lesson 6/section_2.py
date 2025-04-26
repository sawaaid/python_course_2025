# tuple_1=("maher","It",420)
# name,department,salary=tuple_1
# print(name,department,salary)

# t1=(1,5,3)
# t2=(5,1,3)
# print(t1>t2)

# y=(1,7,4,8,7,12,5,7,1)
# print(y[::2])#step
# count=0
# for item in y:
#     if item == 1:
#         count=count+1

# print(count)


employees=[]

def add_emplyee():
    name=input("name")
    age=int(input("age"))
    salary=float(input("salary"))
    department=input("department")
    employees.append((name,salary,department,age))
    print(employees)

def search_emplyee():
    search_name=input("searc name is:")
    for item in employees:
        name,salary,department,age=item
        if name == search_name:
           print(name,salary,department,age)

add_emplyee()
search_emplyee()
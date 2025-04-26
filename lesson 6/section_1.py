#TUPLE
m=("programmer",22,"sa3id")
career,age,name=m
print(career)
t1=(4,5,7,12)
t2=(10,1,0)
print(t1[::-1])

fruits = ("tomato","banana")
# search=input("enter fruit name:")
# print(search in fruits)


e=(1,7,3,7,10,1,2,7)
count=0
for item in e:
    if item == 7:
        count = count+1
print(count)
print(e.count(7))
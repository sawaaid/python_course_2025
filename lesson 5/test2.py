a=dict()
m={"python":44,"android":55}
m["java"]=50
m["python"]=10
a["syria"]=1990
print(a["syria"])

print("syria" in a)
print(1990 in a.values())

for key,value in m.items():
    print(key,value)
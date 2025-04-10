file =open("test1.txt")
name = input("name: ")
for line in file:
    if line.find(name)!=-1:
        print(line)
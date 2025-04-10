file =open("students.txt","r")
count=0
sum=0
for line in file:
    count+=1
    line = line.split("\t")
    mark=int(line[1])
    sum+=mark
print("average is:%f"%(sum/count))

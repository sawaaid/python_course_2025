file = open("test1.txt","r")
count=0
sum=0
for line in file:
    words=line.split("\t")
    count+=1
    mark=int(words[1])
    sum=sum+mark
print("averag: %f" %(sum/count))
  
    

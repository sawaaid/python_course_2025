str = "04:3:20"
index1=str.find(":")
print("h:"+str[0:index1])
index2=str.find(":",index1+1)
print("m:"+str[index1+1:index2])
print("s:"+str[index2+1:])

######################################

s=input("string is:")
def countChar(word,seachChar):
    count=0
    for char in word:
        if char==seachChar:
            count+=1
    return count

for char in s:
    if countChar(s,char)>1:
        print("%s : %g" %(char,countChar(s,char)))
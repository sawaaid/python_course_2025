file = open('lesson 5/4.txt', encoding='UTF-8')
lines = file.readlines()
num=[]
cities=[]
for line in lines:
    words=line.split('\t')
    t=words[2].replace('\n','')
    cities.append(words[0])
    t=t.replace(',','')
    num.append(int(t))
    
print(num)
print(cities)
file1 = open("test1.txt","r")
file2 = open("test2.txt","w")
for line in file1:
    file2.write(line.upper())
file1.close()
file2.close()


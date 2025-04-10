file = open("test1.txt","w")
while True:
    name = input("name: ")
    if name == "end":
        break
    mark = input("mark: ")

    word1 = name + "\t" + mark + "\n"
    file.write(word1)





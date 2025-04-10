file = open("test.txt","w")
while True:
    word = input("word: ")
    if word == "end":
        break
    word1 = word + "\n"
    file.write(word1)





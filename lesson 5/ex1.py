file = open(r"lesson 5/words.txt")
word_dict = dict()

for line in file.readlines():
    words = line.split()
    for word in words:
        word_dict[word] = 1

search_word = input("أدخل كلمة للبحث عنها: ")
if search_word in word_dict:
    print("الكلمة موجودة في الملف.")
else:
    print("الكلمة غير موجودة.")
        
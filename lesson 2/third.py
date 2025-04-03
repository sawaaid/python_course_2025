# أعد كتابة البرنامج السابق في تابع سمّه count بحيث يقبل السلسلة النصية والحرف المراد معرفة مرات تكراره باعتبارهم وسائط.
def count(word,serch_char):
    repeat_count=0
    for letter in word:
        if letter == serch_char:
            repeat_count+=1
    return repeat_count

word=input("enter word: ")
char=input("enter char for count: ")
print(count(word,char))

# أكتب برنامج يطلب من المستخدم إدخال رقم. بعدها يعرض له نسخة من هذا الرقم و لكن بشكل معكوس.

# أكتب برنامج يطلب من المستخدم إدخال رقم. 
# بعدها يعرض له ناتج جمع أعداد هذا الرقم.
try:
    num=int(input("enter number"))
except:
    print("please enter number")
reverseNum=0
while True:
    digit=num%10
    reverseNum = reverseNum*10 + digit
    num = num // 10
    if num == 0:
        break
print(reverseNum)




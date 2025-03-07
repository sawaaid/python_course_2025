# أكتب برنامج يطلب من المستخدم إدخال رقم. 
# بعدها يعرض له ناتج جمع أعداد هذا الرقم.
try:
    num=int(input("enter number"))
except:
    print("please enter number")
sum=0
while True:
    digit=num%10
    sum = sum + digit
    num = num // 10
    if num == 0:
        break
print(sum)




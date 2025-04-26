import socket
import time
# هذا البرنامج يقوم بتنزيل صورة من الإنترنت باستخدام بروتوكول HTTP
# يتم استخدام مكتبة socket لإنشاء اتصال مع الخادم
# يتم إرسال طلب HTTP للحصول على الصورة
# يتم استقبال البيانات وحفظها في ملف صورة محلي
HOST = 'data.pr4e.org'  # اسم الخادم الذي سيتم الاتصال به
PORT = 80  # رقم المنفذ الذي سيتم الاتصال به
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # إنشاء مقبس باستخدام بروتوكول TCP
mysock.connect((HOST, PORT))  # الاتصال بالخادم باستخدام اسم الخادم والمنفذ
mysock.send(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')  # إرسال طلب HTTP لجلب الصورة
count = 0  # متغير لحساب حجم البيانات المستلمة
picture = b""  # متغير لتخزين البيانات المستلمة

while True:  # حلقة لاستقبال البيانات من الخادم
    data = mysock.recv(5120)  # استقبال البيانات بحجم 5120 بايت كحد أقصى
    if len(data) < 1: break  # إنهاء الحلقة إذا لم يتم استقبال بيانات
    #time.sleep(0.25)  # تأخير اختياري بين استقبال البيانات
    count = count + len(data)  # تحديث حجم البيانات المستلمة
    print(len(data), count)  # طباعة حجم البيانات المستلمة في كل مرة
    picture = picture + data  # إضافة البيانات المستلمة إلى المتغير picture

mysock.close()  # إغلاق الاتصال بالمقبس

# Look for the end of the header (2 CRLF)
pos = picture.find(b"\r\n\r\n")  # البحث عن نهاية ترويسة HTTP
print('Header length', pos)  # طباعة طول الترويسة
header = picture[:pos].decode()  # استخراج الترويسة بعد فك ترميزها
print(header)  # طباعة الترويسة

# Skip past the header and save the picture data
picture = picture[pos+4:]  # تجاوز الترويسة والاحتفاظ فقط ببيانات الصورة
fhand = open("stuff1.jpg", "wb")  # فتح ملف جديد لكتابة بيانات الصورة
fhand.write(picture)  # كتابة بيانات الصورة في الملف
fhand.close()  # إغلاق الملف
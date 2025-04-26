
import socket 
"""
هذا البرنامج يقوم بإنشاء اتصال باستخدام مكتبة socket في بايثون لتحميل محتوى نصي من خادم ويب.
الشرح التفصيلي:
1. يتم استيراد مكتبة socket لإنشاء اتصال TCP.
2. يتم إنشاء كائن socket باستخدام بروتوكول IPv4 (AF_INET) وبروتوكول TCP (SOCK_STREAM).
3. يتم الاتصال بالخادم 'data.pr4e.org' على المنفذ 80 (HTTP).
4. يتم إرسال طلب HTTP GET لتحميل الملف النصي 'romeo.txt'.
5. يتم استقبال البيانات من الخادم على دفعات بحجم 512 بايت.
6. يتم فك تشفير البيانات المستلمة وعرضها على الشاشة.
7. يتم إغلاق الاتصال بعد الانتهاء.
"""
 
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
mysock.connect(('data.pr4e.org', 80)) 
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() 
mysock.send(cmd) 
while True: 
    data = mysock.recv(512) 
    if len(data) < 1: 
                         break 
    print(data.decode(),end=' ') 
mysock.close() 

mysock1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock1.connect(("www.google.com",80))
mysock1.send(b"GET http://www.google.com/ HTTP/1.0\r\n\r\n")
while True:
        data = mysock1.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end=' ')
mysock1.close()
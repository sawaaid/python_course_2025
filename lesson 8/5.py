import urllib.request, urllib.parse, urllib.error  # استيراد مكتبة urllib للتعامل مع طلبات HTTP

# فتح رابط الصورة باستخدام urllib
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')

# فتح ملف محلي للكتابة الثنائية (binary) لتخزين الصورة
fhand = open('cover31.jpg', 'wb')

# تهيئة متغير لحساب حجم البيانات المنسوخة
size = 0

# حلقة لقراءة البيانات من الرابط وكتابتها في الملف
while True:
    info = img.read(100000)  # قراءة 100000 بايت من الصورة
    if len(info) < 1: break  # إذا لم يتبق بيانات، إنهاء الحلقة
    size = size + len(info)  # تحديث حجم البيانات المنسوخة
    fhand.write(info)  # كتابة البيانات في الملف

# طباعة حجم البيانات المنسوخة
print(size, 'characters copied.')

# إغلاق الملف
fhand.close()
from bs4 import BeautifulSoup  

# استيراد المكتبات اللازمة للتعامل مع الروابط
import urllib.request, urllib.parse, urllib.error  

# استيراد مكتبة BeautifulSoup لتحليل صفحات HTML

# فتح وقراءة محتوى صفحة الويب
html = urllib.request.urlopen("https://www.aljazeera.net/").read()  

# تحليل محتوى الصفحة باستخدام مكتبة BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')  

# استخراج جميع العلامات <a> من الصفحة
tags = soup('a')  

# التكرار على كل علامة <a>
for tag in tags:  
    # طباعة الرابط الموجود في الخاصية href لكل علامة
    print(tag.get('href', None))  

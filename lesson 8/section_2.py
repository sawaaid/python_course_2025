# import socket
# mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# mySocket.connect(('data.pr4e.org', 80))
# mySocket.send("GET http://data.pr4e.org/cover3.jpg  HTTP/1.0\r\n\r\n".encode())
# dataString = b""
# while True:
#     data = mySocket.recv(5000)
#     if len(data)<1:
#         break
#     print(data)
#     dataString += data

# mySocket.close()
# index = dataString.find(b"\r\n\r\n")
# dataString = dataString[index+4:]
# file = open("jazeera_now.jpg","wb")
# file.write(dataString)
# file.close()

##################
import urllib.request
from bs4 import BeautifulSoup
file = urllib.request.urlopen("https://sp-today.com/en/currency/us_dollar#google_vignette")
data = file.read()
soup = BeautifulSoup(data, "html.parser")
table = soup.find("table",{"class":"table table-hover local-cur"})
rows = table.find_all("tr")
for row in rows:
    cols = row.find_all("td")
    title = row.find("th")
    print(title.text.strip().split("\n")[0],cols[1].text,cols[2].text), 

# كم تبلغ ثروة لامين جمال نجم برشلونة؟
# كيف استخدمت الدعم السريع المسيّرات لتغيير مسار الحرب؟
# الحرب على غزة مباشر.. استشهاد طفلة نتيجة المجاعة والاحتلال يوسع عدوانه
# أكبر فيضان في تاريخ الأرض قبالة المغرب عمره 5 ملايين سنة
# كاتس يحذر الشرع بعد قصف محيط القصر الرئاسي بدمشق
# وظيفة جديدة وراتب سخي للملاكم الأسطوري تايسون
# زعيم المحافظين بكندا خارج البرلمان فهل يدفع ثمن تطرفه؟
# القوات الأميركية تخلي قاعدتين شرقي سوريا
# قتيل وإصابات في غارات إسرائيلية جديدة على سوريا
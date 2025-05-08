# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# mysock.connect(('data.pr4e.org', 80)) 
link = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() 
# mysock.send(link) 
# while True:
#     data=mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(), end='')

# mysock.send(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n') 
# image=b""
# while True:
#     data=mysock.recv(100000)
#     if len(data) < 1:
#         break
#     image = image + data

# pos=image.find(b"\r\n\r\n")

# file=open("image1.jpg","wb")
# file.write(image[pos+4:])


import urllib.request 
from bs4 import BeautifulSoup

# fhand = urllib.request.urlopen('https://www.aljazeera.net/') 
# for line in fhand: 
#     print(line.decode().strip()) 

# import urllib.request
#  
# img = urllib.request.urlopen('https://www.aljazeera.net/wp-content/uploads/2018/01/7938d589-537b-4660-906c-adb12c88a177.jpeg?resize=770%2C513&quality=80').read() 
# fhand = open('cover3.jpg', 'wb') 
# fhand.write(img) 
# fhand.close() 

html = urllib.request.urlopen('https://www.aljazeera.net/news/').read() 

soup = BeautifulSoup(html, 'html.parser') 
lines=soup.find_all("div",{"class":"container--grid"})
for line in lines:
    print(line.text)
    
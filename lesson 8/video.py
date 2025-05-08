# http://data.pr4e.org/romeo.txt
# https://books.islamway.net/1/44/15_MSMunjjid_AreedAtoob.pdf
# https://www.aljazeera.net/wp-content/uploads/2023/11/image-35.jpg?resize=770%2C513&quality=80

# socket
# urllib
# beautifulsoup
import socket
import urllib.request
from bs4 import BeautifulSoup
my_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('data.pr4e.org',80))
url='GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

my_socket.send(url)

file=b""
while True:
    data=my_socket.recv(512)
    if len(data)<1:
        break
    file = file + data
    print(data.decode())

my_socket.close()

pos=file.find(b"\r\n\r\n")

file1=open("text.txt","wb")
file1.write(file[pos+4:])
file1.close()

flines=urllib.request.urlopen("https://www.aljazeera.net/")
soub=BeautifulSoup(flines, 'html.parser')
all_a = soub('h3')
for link in all_a:
        print(link)




from bs4 import BeautifulSoup  
import urllib.request, urllib.parse, urllib.error  

html = urllib.request.urlopen("https://www.aljazeera.net/").read()  
soup = BeautifulSoup(html, 'html.parser')  
tags = soup('h3',{"class":"card-collection-flat__title-header"})  

for tag in tags: 
    # print('TAG:', tag)  
    # print('URL:', tag.get('href', None)) 
    print('Contents:', tag.text) 
    # print('Attrs:', tag.attrs) 

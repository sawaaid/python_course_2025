import urllib.request
 
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read() 
fhand = open('cover3.jpg', 'wb') 
fhand.write(img) 
fhand.close() 
import urllib.request
from bs4 import BeautifulSoup
page = urllib.request.urlopen('https://www.aljazeera.net/where/arab/syria/')
soub = BeautifulSoup(page)
news = soub.find_all("h3",{"class":"gc__title"})
for item in news:
    print(item.text)


# 11900 12000 دولار أمريكي دمشق
# 11900 12000 دولار أمريكي حلب
# 11900 12000 دولار أمريكي إدلب
# 12200 12300 دولار أمريكي الحسكة

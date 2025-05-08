# هذا البرنامج يقوم بجلب أسعار صرف الدولار الأمريكي من صفحة ويب معينة

import urllib.request
from bs4 import BeautifulSoup
page = urllib.request.urlopen('https://www.sp-today.com/currency/us_dollar#google_vignette')
soup = BeautifulSoup(page, 'html.parser')
table = soup.find('table', {'class': 'table table-hover local-cur'})
rows = table.find_all('tr')
for  row in rows:
    cols = row.find_all('td')
    title = row.find('th').text.strip().split("\n")
    print([cols[2].text.strip() ,cols[1].text.strip() ,title[0]]) 

# ['11900', '11800', 'دولار أمريكي دمشق']
# ['11900', '11800', 'دولار أمريكي حلب']
# ['11900', '11800', 'دولار أمريكي إدلب']
# ['12100', '12000', 'دولار أمريكي الحسكة']
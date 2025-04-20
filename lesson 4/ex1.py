file= open('lesson 4/1 (2).txt',encoding='UTF-8')
lines=file.readlines()
cities=[]
num=[]
for line in lines:
    cols=line.split('\t')
    print(cols[2].replace(',',''))
    try:
       cities.append(int(cols[2].replace(',','')))
    except:
       print(cols[2].replace(',',''))
    finally:
       num.append(cols[0])

print(cities)

# https://drsc-sy.org/%D8%AC%D8%AF%D8%A7%D9%88%D9%84-%D9%88%D8%AE%D8%B1%D8%A7%D8%A6%D8%B7-%D8%A7%D8%AD%D8%B5%D8%A7%D8%A6%D9%8A%D8%A9-%D9%84%D8%B6%D8%AD%D8%A7%D9%8A%D8%A7-%D8%AC%D8%B1%D8%A7%D8%A6%D9%85-%D8%A7%D9%84%D9%86/


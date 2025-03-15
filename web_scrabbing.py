import requests

url = "https://www.google.com/"  # ضع رابط الموقع هنا
response = requests.get(url)

if response.status_code == 200:  # التحقق من نجاح الطلب
    print(response.text[748:800])  # طباعة محتوى الصفحة HTML
else:
    print(f"فشل الطلب: {response.status_code}")

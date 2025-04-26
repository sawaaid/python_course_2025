import re
text = "You can reach us at 123-456-7890 or 987.654.3210."

m=re.findall(r"\d{3}[-.]\d{3}[-.]\d{4}", text)

print(m)


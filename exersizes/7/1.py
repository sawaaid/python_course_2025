import re

text = "Please contact us at support@example.com or sales@company.org for assistance."

y = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+", text)

print(y)

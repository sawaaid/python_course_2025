import re
password = "Secure123"
has_upper = re.search(r"[A-Z]", password)
has_lower = re.search(r"[a-z]", password)
has_digit = re.search(r"[0-9]", password)
long_enough = len(password) >= 8

# تحقق نهائي
if has_upper and has_lower and has_digit and long_enough:
    print("true")
else:
    print("re enter")
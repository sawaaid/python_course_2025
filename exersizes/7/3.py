import re
text = "Ali and Sara went to Paris and met John in London."
print(re.findall(r"[A-Z][a-z]+",text))
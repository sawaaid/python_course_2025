import re

text = "cat cut cot c9t cast ct cait"
matches = re.findall(r"c.t", text)

print(matches)
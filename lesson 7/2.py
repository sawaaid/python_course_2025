import re

text = "hello   world hello world  helloworld"
matches = re.findall(r"hello\s*world", text)

print(matches)


import re

text = "hello   world hello world  helloworld"
matches = re.findall(r"hello\s+world", text)

print(matches)

import re

lines = [
    "From: user@example.com",
    "To: admin@example.com",
    "From:admin@test.org",
    "From someone@example.com",
    "From: someone@example.com"
]

for line in lines:
    if re.search(r'^From:.+@', line):
        print("Match found:", line)


import re 
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM' 
lst = re.findall('\S+@\S+', s) 
print(lst)

import re

x = 'We just received $10.00 for cookies.'
y = re.findall(r'\$[0-9.]+', x)
print(y)  # الناتج: ['$10.00']
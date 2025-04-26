import re
text="cat cot cet ct ctas ccctasd catjjs"
print(re.findall("c+t",text))


text = "hello   world hello world  helloworld"
print(re.findall("hello\s*world",text))

lines = [
 "ee From: user@example.com",
 "To: admin@example.com",
 "From:admin@test.org",
 "From someone@example.com",
 "From: someone@example.com"
]
for item in lines:
    print(re.findall("^From: \S+@\S+",item))


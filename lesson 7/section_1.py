import re
text = "cat cot cet ct actsn cattsgha"
list1=re.findall("c.t",text)
print(list1)
# ['cat', 'cot', 'cet', 'cat']

text = "cat cot cet ct actsn cattsgha"
list1=re.findall("m*t",text)
print(list1)
# ['t', 't', 't', 't', 't', 't', 't']

text = "cat cot cet ct acmmtsn cmttsgha"
list1=re.findall("m+t",text)
print(list1)
# ['t', 't', 't', 't', 't', 't', 't']

text = "tcat cot cet ct acmmtsn cmttsgha"
list1=re.findall("\sc.t\s",text)
print(list1)
# ['t', 't', 't', 't', 't', 't', 't']


lines = [
  "From: user@example.com",
  "To: admin@example.com",
  "From:admin@test.org",
  "From someone@example.com",
  "From: someone@example.com",
  "From:@google.com"]
for line in lines:
  if re.search(r'^From:.+@', line):
    print("Match found:", line)


lines = [
  "From: user@example.com",
  "To: admin@example.com",
  "From:admin@test.org",
  "From someone@example.com",
  "From: someone@example.com",
  "From: @google.com"]
for line in lines:
    if re.search('\S+@\S+', line):
        print("Match found:", line)

    
    text="345 456 4558"
    print(re.findall("\d{3}[-\s.]\d{3}",text))

    text="he get $.1003 "
    print(re.findall("\$[0-9.]+",text))

    text = "Please contact us at support@example.com or sales@company.org for assistance."
    y=re.findall("[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+",text)
    print(y)

    text = "Ali and Sara went to Paris and met John in London."
    print(re.findall(r"\b[A-Z][a-z]+",text))



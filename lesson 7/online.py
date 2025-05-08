import re
text='''Hello, my name is John_Doe123 and my email is john.doe@example.com.  
You can also reach me at work: john_doe@company.co.uk or call me at +1 (555) 123-4567.  
My backup number is 555.765.4321 or just 5557654321.

Today is 2025-05-07, but I also wrote this on 07/05/2025 and 05-07-25.  
Visit our website at https://www.example.com or http://blog.example.org/page?id=123.  
Don't forget to This check out www.test-site.net.

Some product SKUs: ABC-123, xyz_456, and PROD99.  
Prices are listed as $19.99, €29, or ¥3500.  
Random values: 42, -17, 3.14159, 0.0001

# Tags: #regex, #testing, #123  
Special chars: !@#$%^&*()_+-=[]{}|;:'",.<>/?`~  
Multiline  
test:  
This. is line one.  
This is line two.  
Those
End of sample!
'''
#  regex

lines = re.findall(r"\d{2}[-/]\d{2}",text)
for line in lines:
    print(line)

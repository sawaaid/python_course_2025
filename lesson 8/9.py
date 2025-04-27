import re
html_text = '''<h1>The First Page</h1>
<p>
If you like, you can switch to the
<a href="http://www.dr-chuck.com/page2.htm">
Second Page</a>.
</p>'''
print(re.findall("https*://.+",html_text))
import re

text = "this is 255 and 747"
finds = re.search('\d\d\d', text)

print(finds.group())

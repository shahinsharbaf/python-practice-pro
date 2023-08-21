import re

my_regex = re.compile(r'a+')
text = "12aaa 1aa23 12a345"

mo = my_regex.findall(text)

if (mo == None):
    print("not found")
else:
    print(mo)

import re

text = """what is new in python 3.10
Release 3.10.1 g
Date january 10,2022
Editor
Pablo Galindo Salgado
This article explain the new features in python 3.10, compared to 3.9.
"""

my_reg = re.compile(r'3\S+')
mo = my_reg.findall(text)
print(mo)


url = 'https://www.apmillers.com/new/daily/wp/2022/02/02/regular-experision-patterns/'

my_reg2 = re.compile(r'(\d{4})/(\d{1,2})/(\d{1,2})')
res = my_reg2.findall(url)
print(res)

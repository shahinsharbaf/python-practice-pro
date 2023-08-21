import re

text = """"The use of 1234 to say "I love you"
comes from the following ideas: i have 1 thing 2
say: 3words 4 you"""

my_reg = re.compile(r'\d+\s\w+')

mo = my_reg.findall(text)

print(mo)

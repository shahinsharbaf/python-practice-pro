import re


def text_match(text):
    my_reg = re.compile(r'[c|C]\w+[e|E]')
    res = my_reg.findall(text)
    return (res)


text = "I become to CTRE every year"
print(text_match(text))

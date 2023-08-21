import re


def extract_email(text):
    my_reg = re.compile(r'\w+@[a-z]+\.com', re.MULTILINE)
    res = my_reg.findall(text)
    return res


text = """From test@appmillers.com wen jan 09:14:15 2022\nFrom info@appmillers.com wen jan 5 09:15:24\n from elshad@appmillers.com wen jan"""

print(extract_email(text))

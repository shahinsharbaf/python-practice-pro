import re


def find_word(text):
    my_reg = re.compile(r'\b\w{3,5}\b')
    res = my_reg.findall(text)
    return res


my_text = """I like Python for everone course. It is the best one out there."""

print(find_word(my_text))

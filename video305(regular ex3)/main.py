import re


def check_char(my_string):
    my_string2 = ""

    for item in my_string:
        if item == '*' or item == "+" or item == '?':
            my_string2 += "\\"+item+'|'
        else:
            my_string2 += item+'|'
    my_string2 = my_string2[:-1]
    text = 'ABCDEFGHIJKLMNOPQRSTUYXZabcdefghijklmnopqrstuxyz0123456789'
    my_reg = re.compile(my_string2)
    mo = my_reg.findall(text)
    print(mo)


def check_char2(text):
    my_reg = re.compile(r"[a-z]|[A-Z]|[0-9]")
    mo = my_reg.findall(text)
    print(mo)


check_char("ABCDEFabef125")
check_char("*&%@#")

check_char2("ABCDEFabef125")
check_char2("*&%@#")

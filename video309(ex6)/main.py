import re


def text_match(text):
    my_reg = re.compile(r'^[A-Z]+_[A-Z]+$')
    res = my_reg.findall(text)
    return (res)



if text_match("ASXN_CCSDCFa") == []:
    print('Not Matched')
else:
    print("Matched")

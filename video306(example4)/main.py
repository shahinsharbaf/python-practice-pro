
import re

text = "The following example creates a list with 50 elements. All elements are then added to the list when the list is created."


def start_ae(text):
    my_reg = re.compile(r'[e|a]\w+')
    mo = my_reg.findall(text)
    return mo


print(start_ae(text))

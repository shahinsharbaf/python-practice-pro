import random

name_list = []

while True:
    name = input("Enter your name: ")
    if name == "done":
        break
    name_list.append(name)


def rnd_list(list):
    list_length = len(list)
    print("pay: %s" % list[random.randint(0, list_length-1)])


rnd_list(name_list)

list = [5, 88, 66, 22, 44, 51, 78, 35, 150, 55, 76]


def numbers_div_by_five(list):
    for number in list:
        if (number > 130):
            print("STOP")
            break
        if (number % 5 == 0):
            print("this number can divide 5: %i" % number)


numbers_div_by_five(list)

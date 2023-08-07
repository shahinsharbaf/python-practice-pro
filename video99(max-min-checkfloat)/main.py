list_num = [15, 12.5, 14.8, 18.5, "ali", 16]


def check_float_num(number):
    try:
        number = float(number)
    except:
        return False
    else:
        return number


def max_min(list):
    max = min = list[0]
    for number in list:
        if (type(check_float_num(number)) is float):
            if (number > max):
                max = number
            if (number < min):
                min = number
    return (max, min)


print(max_min(list_num))

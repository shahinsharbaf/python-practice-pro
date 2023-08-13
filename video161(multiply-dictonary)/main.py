def multiply_values(my_dictinary):
    multiply = 1
    for key in my_dictinary:
        multiply *= my_dictinary[key]
    return multiply


my_dic = {"one": 1, "two": 2, "there": 3, "four": 4, "five": 5}
print(multiply_values(my_dic))

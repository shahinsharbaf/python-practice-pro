my_tuple = ("a", "b", "c", "d", "e", "a", "c",
            "e", "b", "e", "c", "a", "f", "e", "r")


def most_frequent(tuple):
    my_dic = {}
    for item in tuple:
        if item in my_dic:
            my_dic[item] += 1
        else:
            my_dic[item] = 1
    ferquent = 0
    my_data = ""
    for key, value in my_dic.items():
        if value > ferquent:
            my_data = key
            ferquent = value
    return ferquent, my_data


print(most_frequent(my_tuple))

my_dictionary = {
    "name": "edy",
    "age": 30,
    "salary": 5000,
    "city": "london"
}


def change_dictinary_key(my_dic):
    my_dic["address"] = my_dic.pop("city", None)
    return my_dic


print(change_dictinary_key(my_dictionary))

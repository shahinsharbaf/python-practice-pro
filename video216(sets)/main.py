my_list = [3, 4, 5, 1, 1, 3, 4, 9, 8]


def adding_set(input_list):
    my_set = set()
    for item in input_list:
        my_set.add(item)
    return my_set


print(adding_set(my_list))

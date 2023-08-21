my_list = ["apple", "apple", "orange", "grape", "grape", "orange", "apple"]


def remove_duplicated_set(input_list):
    my_set = set()
    for item in my_list:
        my_set.add(item)
    return my_set


print(remove_duplicated_set(my_list))

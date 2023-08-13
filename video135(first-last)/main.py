my_list = ['cbc', 'xyz', 'aba', '2332', 'abc']


def count_words(list):
    count = 0
    for item in list:
        if len(item) >= 3:
            item_length = len(item)
            if item[0] == item[item_length-1]:
                count += 1
    return count


print(count_words(my_list))

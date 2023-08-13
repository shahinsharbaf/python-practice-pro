list1 = [1, 2, 3, 4, 5]


def custom_insert(list, number):
    temp_list = list[:]
    temp_list.append(number)
    print(temp_list)


custom_insert(list1, 6)
print(list1)

custom = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def reverse(list):
    new_list = []
    new_list.extend(list)
    for i in range(len(list)):
        new_list[i] = list[len(list)-i-1]
    return new_list


def reverse_slice(list):
    new_list = []
    length_list = len(list)
    for i in range(length_list):
        new_list.extend(list[length_list-i-1:length_list-i])
    return new_list


print(reverse(custom))
print(reverse_slice(custom))

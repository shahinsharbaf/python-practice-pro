my_list = [10, 10, 5, 15, 50, 50]

for i in range(len(my_list)):
    if my_list[i] == 50:
        my_list[i] = 5
        break


print(my_list)

def square_list(list):
    for i in range(len(list)):
        list[i] = list[i]*list[i]


custom = [1, 2, 3, 4, 5]
square_list(custom)
print(custom)

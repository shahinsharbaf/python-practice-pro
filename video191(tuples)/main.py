my_tuple = (10, 40, 80, 90)

sum = 0
count = 0
for item in my_tuple:
    count += 1
    sum += item
    print(item, end='')
    if count == len(my_tuple):
        break
    print(end=' + ')


print(' = %i' % sum)

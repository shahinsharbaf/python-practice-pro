my_number = input("Enter a number? ")
sum = 0

try:
    my_number = int(my_number)
except:
    print("not valid")
else:
    my_number = str(my_number)
    for number in my_number:
        sum += int(number)

if (sum != 0):
    print(sum)

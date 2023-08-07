sum = 0
count = 0
num = input("Enter number? ")
while num != "done":
    try:
        num = int(num)
    except:
        print("just Enter number!! ")
        num = input("Enter number? ")
    else:
        sum += num
        count += 1
        num = input("Enter number? ")
if (count != 0):
    print(sum/count)
else:
    print(0)

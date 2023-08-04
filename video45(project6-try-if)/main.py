salary = 0
try:
    hour = int(input("Enter hours? "))
    rate = int(input("Enter rate? "))
except:
    print("not valid")
else:
    if (hour <= 40):
        salary = round(hour*rate, 2)
        print(f"salary is {salary}")
    else:
        salary = round(((40 * rate) + (hour-40)*rate*1.5), 2)
        print(f"salary is {salary}")

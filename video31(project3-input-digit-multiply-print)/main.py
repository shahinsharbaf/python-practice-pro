hours = input("Enter Hours? ")
rate = input("Enter rate? ")
print("pay %0.2f" % (float(hours)*float(rate)))
print("second algorithm")
pay = round(float(hours)*float(rate), 2)
print(f"pay is {pay}")

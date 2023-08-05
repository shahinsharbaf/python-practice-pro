def convert_ounce_milimetre(ounce):
    print("result %f" % (ounce*29.57353))


try:
    ounce = int(input("Enter ounce amount? "))
except:
    print("not valid")
else:
    convert_ounce_milimetre(ounce)

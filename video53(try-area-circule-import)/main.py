import math

try:
    radius = float(input("Enter radious? "))
except:
    print("not valid")
    quit()

print("The area of circule %0.2f" % (radius ** 2 * math.pi))

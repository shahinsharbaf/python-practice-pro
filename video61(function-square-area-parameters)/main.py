def square_area(edge):
    return edge*edge


try:
    edge = int(input("Enter the edge size? "))
except:
    print("not valid")
else:
    print("area is %i" % (edge*edge))

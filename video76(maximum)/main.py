# def max(n1, n2, n3):
#     if n1 > n2:
#         if n1 > n3:
#             return n1
#         else:
#             return n3
#     if n2 > n3:
#         return n2
#     else:
#         return n3


# try:
#     n1 = int(input("Enter first number? "))
#     n2 = int(input("Enter secondnumber? "))
#     n3 = int(input("Enter third number? "))
# except:
#     print("not valid")
# else:
#     print(max(n1, n2, n3))

def max_two_number(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2


def max_there_number(n1, n2, n3):
    return max_two_number(max_two_number(n1, n2), n3)


try:
    n1 = int(input("Enter first number? "))
    n2 = int(input("Enter secondnumber? "))
    n3 = int(input("Enter third number? "))
except:
    print("not valid")
else:
    print(max_there_number(n1, n2, n3))

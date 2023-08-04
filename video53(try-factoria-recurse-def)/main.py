try:
    num = int(input("Enter number? "))
except:
    print("not valid")
    quit()

factorial = 0


def fac(n):
    if n == 1:
        return 1
    return n*fac(n-1)


print("factor %i" % fac(num))

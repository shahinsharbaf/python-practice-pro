def factorial(facrorial_num):
    if facrorial_num < 0:
        return ("factoria does not exist")
    elif facrorial_num == 0:
        return (1)
    result = 1
    for num in range(1, facrorial_num+1):
        result = result * num
    return ("the factorial of %i is %i" % (facrorial_num, result))


try:
    factorial_num = int(input("Enter factorial num: "))
except:
    print("not valid")
else:
    print(factorial(factorial_num))

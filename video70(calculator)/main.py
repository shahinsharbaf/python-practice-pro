try:
    first_num = int(input("What is the first number? "))
    second_num = int(input("Whai is thesecond number? "))
except:
    print("not valid")
else:
    operation = input("pick operation from this list (+-*/)? ")


def calculator(first_num, second_num, operation):
    if operation == '+':
        return (first_num+second_num)
    if operation == '-':
        return (first_num-second_num)
    if operation == '*':
        return (first_num*second_num)
    if operation == '/':
        if (second_num != 0):
            return (first_num/second_num)
        else:
            return("divide by zero!!!!")
    return ("not valid operation")


print(calculator(first_num, second_num, operation))

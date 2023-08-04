try:
    salary = int(input("What is your salary? "))
except:
    print("not valid input")
else:
    print("you salary is %i" % salary)
finally:
    print("good day")

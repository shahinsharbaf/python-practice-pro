def pass_controller(password):
    if len(password) < 8:
        return False
    return True


password = input("Enter pass? ")
if pass_controller(password) == True:
    print("pass is strong")
else:
    print("password is weak")

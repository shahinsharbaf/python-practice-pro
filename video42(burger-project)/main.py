print("Welcome to burger shop")
burger = input("What size burger do you want? M,N, or L ")
mashrom = input("Do you want mushroom? Y or N ")
cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if burger.capitalize() == 'M':
    bill = 5
    if mashrom.capitalize() == 'Y':
        bill = bill + 1
elif burger.capitalize() == 'N':
    bill = 8
    if mashrom.capitalize() == 'Y':
        bill = bill+1
elif burger.capitalize() == 'L':
    bill = 10
    if mashrom.capitalize() == 'Y':
        bill = bill+2
else:
    print("not valid")
if cheese.capitalize() == 'Y':
    bill = bill+1

print("you bill is %i" % bill)

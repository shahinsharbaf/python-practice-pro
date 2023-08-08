import random
number_of_dices = 2


def roll_the_dice():
    return (random.randint(1, 6))


for item in range(0, number_of_dices):
    print(roll_the_dice())

while True:
    roll_again = input("Roll the dice again?(Y,N) ")
    if (roll_again.upper() == "Y"):
        for item in range(0, number_of_dices):
            print(roll_the_dice())
    elif (roll_again.upper() == "N"):
        break
    else:
        print("not valid!!")

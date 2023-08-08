import random


def user_computer_choices():
    rock_scissors_rock = ["rock", "scissors", "paper"]
    while True:
        user_choice = input("Enter you choice (rock,scissors,paper)? ")
        if user_choice.lower() == "rock" or user_choice.lower() == "scissors" or user_choice.lower() == "paper":
            com_choice = rock_scissors_rock[random.randint(0, 2)]
            return user_choice, com_choice
        else:
            print("not valid")


def rock_paper_scissors(user_choice, com_choice):
    if user_choice == com_choice:
        return ("computer choiced: "+com_choice + " and " "user choiced: " + user_choice + " result is: " + "equal")
    if ((user_choice == "rock" and com_choice == "scissors") or (user_choice == "scissors" and com_choice == "paper") or (user_choice == "paper" and com_choice == "rock")):
        return ("computer choiced: "+com_choice + " and " "user choiced: " + user_choice + " result is: " + "user win")
    return ("computer choiced: "+com_choice + " and " "user choiced: " + user_choice + " result is: " + "computer win")


while True:
    user_choice, com_choice = user_computer_choices()
    print(rock_paper_scissors(user_choice, com_choice))
    tryagain = input("play again?(Y,N) ")
    if tryagain.capitalize() == "N":
        break

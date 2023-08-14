import os


os.system('cls')


def get_blind_auction():
    user_name = input("What is you name? ")
    bid_amount = int(input("What is you bid amount? $"))
    return (user_name, bid_amount)


bids_amount_dictinary = {}
while True:
    user_name, bid_amount = get_blind_auction()
    bids_amount_dictinary[user_name] = bid_amount
    if input("Are there any bider?(Y,N) ").upper() == "N":
        break
    os.system('cls')

max = 0
bider = ""
for key, value in bids_amount_dictinary.items():
    if (value > max):
        max = value
        bider = key

print("The wineer is %s with a bid of $%i" % (bider, max))

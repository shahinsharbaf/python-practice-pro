class Money:
    def __init__(self, amount) -> None:
        self.amount = amount

    def get_bet(self, max_amount):
        my_bet = int(input("Enter bet? "))
        while my_bet > max_amount:
            print("not promise upper than you money? ")
        return my_bet

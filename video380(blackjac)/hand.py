
class Hand:
    def __init__(self, dealer= False) -> None:
        self.dealer = dealer
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        for item in self.cards:
            if item[1]=="J":
                self.value+=
            if item[1]=="Q":
                pass
            if item[1]=="K":
                pass
            if item[1]=="A":
                pass
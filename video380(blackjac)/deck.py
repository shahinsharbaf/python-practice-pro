import random


class Deck:
    def __init__(self) -> None:
        self.cards = []
        for j in ('heart', 'diamond', 'club', 'spade'):
            for i in range(2, 11):
                self.cards += [(j, i)]
            for k in ("A", "J", "Q", "K"):
                self.cards += [(j, k)]

    def shuffle(self):
        shuffled_cards = []
        cards_count = 52
        while cards_count != 0:
            random_card = random.randint(0, cards_count-1)
            shuffled_cards.append(self.cards[random_card])
            self.cards.remove(self.cards[random_card])
            cards_count -= 1
        self.cards = shuffled_cards

    def deal(self):
        return (self.cards.pop())

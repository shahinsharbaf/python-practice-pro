from money import Money
from deck import Deck
from hand import Hand
import sys

print("welcome to game")

money = Money(5000)

while True:
    if money.amount <= 0:
        print("Thanks for playing!")
        sys.exit()
    print("Money: ", money.amount)
    bet = money.get_bet(money.amount)
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand(True)

    for i in range(2):
        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

    print("Bet ", bet)

    while True:
        

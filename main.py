import random

suits = ('HEARTS', 'DIAMONDS', 'SPADES', 'CLUBS')
ranks = ('TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING', 'ACE')
values = {'TWO':2, 'THREE':3, 'FOUR':4, 'FIVE':5, 'SIX':6, 'SEVEN':7, 'EIGHT':8,
          'NINE':9, 'TEN':10, 'JACK':11, 'QUEEN':12, 'KING':13, 'ACE':14}

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " OF " + self.suit

class Deck:

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"PLAYER {self.name} HAS {len(self.all_cards)} CARDS."

player_one = Player("ONE")
player_two = Player("TWO")

new_deck = Deck()
new_deck.shuffle()

for i in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

import pdb

game_on = True

round_num = 0

while game_on:

    round_num += 1
    print(f"ROUND {round_num}!\n")

    if len(player_one.all_cards) == 0:
        print("PLAYER ONE OUT OF CARDS! GAME OVER!\n")
        print("PLAYER TWO WINS!\n")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("PLAYER TWO OUT OF CARDS! GAME OVER!\n")
        print("PLAYER ONE WINS!\n")
        game_on = False
        break

    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:

        print(f"{player_one_cards[-1]} VS. {player_two_cards[-1]}\n")

        if player_one_cards[-1].value > player_two_cards[-1].value:

            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            print("PLAYER ONE WINS!\n")

            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:

            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)

            print("PLAYER TWO WINS!\n")

            at_war = False

        else:

            print("WAR!\n")

            if len(player_one.all_cards) < 5:
                print("PLAYER ONE UNABLE TO PLAY WAR! GAME OVER AT WAR!\n")
                print("PLAYER TWO WINS! PLAYER ONE LOSES!\n")

                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("PLAYER TWO UNABLE TO PLAY WAR! GAME OVER AT WAR!\n")
                print("PLAYER ONE WINS! PLAYER TWO LOSES!\n")

                game_on = False
                break

            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
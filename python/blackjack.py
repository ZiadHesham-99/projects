import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + "  of  " + self.suit


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
       return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.balance = 100
        self.bitA = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

    def bit(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            self.bitA += amount

        else:
            print("your current balance is not enough")




    def earn(self,amount):
        self.balance += amount

    def show_value(self):
        return self.value

    def show_balance(self):
        return self.balance

    def reset(self):
        self.cards = []
        self.value = 0
        self.bitA = 0



def hit(deck,hand):
    card = deck.deal()
    hand.add_card(card)
    print(card)


def player_busts(player):
    if player.value > 21 :
        return True
    else:
        return False


def player_wins():
    pass


def dealer_busts(computer):
    if computer.value > 21:
        return True
    else:
        return False


def dealer_wins(player,computer):
    if computer.value > player.value and computer.value < 21:
        return  True
    else:
        return False



print("Hello in ziad black jack game !")
my_deck = Deck()
my_deck.shuffle()
player = Hand()
computer = Hand()
while True:
    Y = int(input("please enter a bit"))
    player.bit(Y)
    computer.bit(Y)
    print("the player is dealt :")
    for X in range(2):
        hit(my_deck, player)
    print("the computer is dealt :")
    hit(my_deck, computer)
    print("the computer value equals:")
    print(computer.show_value())
    computer.add_card(my_deck.deal())
    print("the player value equals : ")
    print(player.show_value())
    while True:
        X = int(input("press 1 to hit and 2 to stay"))
        if X == 1:
            hit(my_deck, player)
            print("the player value equals : ")
            print(player.show_value())
        else:
            break
    if player_busts(player) == True:
        print("computer won")
        computer.earn(Y * 2)
    else:
        if dealer_wins(player, computer) == True:
            print("computer won")
            computer.earn(Y * 2)
        else:
            while True:
                hit(my_deck, computer)
                print("computer value equals: ")
                print(computer.show_value())
                if dealer_wins(player, computer) == True:
                    print("computer won")
                    computer.earn(Y * 2)
                    break
                if dealer_busts(computer) == True:
                    print("Player won")
                    player.earn(Y * 2)
                    break
                else:
                    pass
    print("The player balance : ")
    print(player.show_balance())
    print("The computer balance : ")
    print(computer.show_balance())
    player.reset()
    computer.reset()
    Z = int(input("do u wana play again 1 for yes 2 for no"))
    if Z == 1:
        pass
    else:
        break
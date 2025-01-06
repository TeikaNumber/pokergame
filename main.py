import os
import random

#Classes

class Card:
    def __init__(self, rank, suit, modifier):
        self.rank = rank
        self.suit = suit
        self.modifier = modifier

    def suit_to_ascii(image, suit):
        if suit == "d":
            image.append(r"|  /\  |")
            image.append(r"|  \/  |")
        elif suit == "s":
            image.append(r"|  /\  |")
            image.append("|  VV  |")
        elif suit == "h":
            image.append("|  AA  |")
            image.append(r"|  \/  |")
        elif suit == "c":
            image.append("|  oo  |")
            image.append("|  qp  |")
        return image
    
    def card_to_ascii(rank, suit, modifier):
        image = ["--------"]
        if rank < 11 and rank > 1 and modifier == "none":
            image.append(f"|{rank}     |")
            image = suit_to_ascii(image, suit)
            image.append(f"|     {rank}|")
        elif rank == 1:
            image.append("|A     |")
            image = suit_to_ascii(image, suit)
            image.append("|     A|")
        image.append("--------")
        return image
    
    def __str__(self):
        if self.modifier == "none":
            return f"{self.suit}{self.rank}"
        else:
            return f"{self.suit}{self.rank} {self.modifier}"

class Deck:
    def __init__(self, cards: list):
        self.length = len(cards)
        self.containedCards = cards

    def __str__(self):
        strng = ""
        for i in self.containedCards:
            strng += str(i) + " "
        return strng

#Functions
def print_hand(hand):
    art = []
    for i in range(len(hand)): #for every card in hand
        art.append(hand[i].card_to_ascii) #add an image of that card
    for i in range(6):
        line = '   '.join([])

#Variables

'''Create Starting Deck'''
list = []
list.append(Card(1, 'h', 'none'))
list.append(Card(2, 'h', 'none'))
list.append(Card(3, 'h', 'none'))
list.append(Card(4, 'h', 'none'))
list.append(Card(5, 'h', 'none'))
list.append(Card(6, 'h', 'none'))
list.append(Card(7, 'h', 'none'))
list.append(Card(8, 'h', 'none'))
list.append(Card(9, 'h', 'none'))
list.append(Card(10, 'h', 'none'))
list.append(Card(11, 'h', 'none'))
list.append(Card(12, 'h', 'none'))
list.append(Card(13, 'h', 'none'))
list.append(Card(1, 's', 'none'))
list.append(Card(2, 's', 'none'))
list.append(Card(3, 's', 'none'))
list.append(Card(4, 's', 'none'))
list.append(Card(5, 's', 'none'))
list.append(Card(6, 's', 'none'))
list.append(Card(7, 's', 'none'))
list.append(Card(8, 's', 'none'))
list.append(Card(9, 's', 'none'))
list.append(Card(10, 's', 'none'))
list.append(Card(11, 's', 'none'))
list.append(Card(12, 's', 'none'))
list.append(Card(13, 's', 'none'))
list.append(Card(1, 's', 'none'))
list.append(Card(2, 's', 'none'))
list.append(Card(3, 's', 'none'))
list.append(Card(4, 's', 'none'))
list.append(Card(5, 's', 'none'))
list.append(Card(6, 's', 'none'))
list.append(Card(7, 's', 'none'))
list.append(Card(8, 's', 'none'))
list.append(Card(9, 's', 'none'))
list.append(Card(10, 's', 'none'))
list.append(Card(11, 's', 'none'))
list.append(Card(12, 's', 'none'))
list.append(Card(13, 's', 'none'))
list.append(Card(1, 'c', 'none'))
list.append(Card(2, 'c', 'none'))
list.append(Card(3, 'c', 'none'))
list.append(Card(4, 'c', 'none'))
list.append(Card(5, 'c', 'none'))
list.append(Card(6, 'c', 'none'))
list.append(Card(7, 'c', 'none'))
list.append(Card(8, 'c', 'none'))
list.append(Card(9, 'c', 'none'))
list.append(Card(10, 'c', 'none'))
list.append(Card(11, 'c', 'none'))
list.append(Card(12, 'c', 'none'))
list.append(Card(13, 'c', 'none'))
deck = Deck(list)

hand = Deck([])
print_hand(hand)
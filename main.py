import os
import random

#Classes

class Card:
    def __init__(self, rank, suit, modifier):
        self.rank = rank
        self.suit = suit
        self.modifier = modifier

    def suit_to_ascii(self, image):
        if self.suit == "d":
            image.append(r"|  /\  |")
            image.append(r"|  \/  |")
        elif self.suit == "s":
            image.append(r"|  /\  |")
            image.append("|  VV  |")
        elif self.suit == "h":
            image.append("|  AA  |")
            image.append(r"|  \/  |")
        elif self.suit == "c":
            image.append("|  oo  |")
            image.append("|  qp  |")
        return image
    
    def card_to_ascii(self):
        image = ["--------"]
        if self.modifier != "wild":
            if self.rank < 11 and self.rank > 1:
                image.append(f"|{self.rank}     |")
                image = self.suit_to_ascii(image)
                image.append(f"|     {self.rank}|")
            elif self.rank == 1:
                image.append("|A     |")
                image = self.suit_to_ascii(image)
                image.append("|     A|")
            elif self.rank == 11:
                image.append("|J     |")
                image = self.suit_to_ascii(image)
                image.append("|     J|")
            elif self.rank == 12:
                image.append("|Q     |")
                image = self.suit_to_ascii(image)
                image.append("|     Q|")
            elif self.rank == 13:
                image.append("|K     |")
                image = self.suit_to_ascii(image)
                image.append("|     K|")
        image.append("--------")
        return image
    
    def __str__(self):
        if self.modifier == "none":
            return f"{self.suit}{self.rank}"
        else:
            return f"{self.suit}{self.rank} {self.modifier}"

class Deck:
    def __init__(self, cards: list):
        
        self.containedCards = cards

    @property
    def length(self):
        return len(self.containedCards)

    def __str__(self):
        strng = ""
        for i in self.containedCards:
            strng += str(i) + " "
        return strng

#Functions

def print_hand(hand):
    art = []
    for i in range(hand.length): #for every card in hand
        art.append(hand.containedCards[i].card_to_ascii()) #add an image of that card

    for i in range(6):
        line = ""
        for j in range(hand.length):
            line += art[j][i]
            if j + 1 != hand.length:
                line += "   "
        print(line)

#Variables

#Create Starting Deck v
#region
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
#endregion

hand = Deck([Card(12,'d','none'), Card(11,"c","none")])
print_hand(hand)

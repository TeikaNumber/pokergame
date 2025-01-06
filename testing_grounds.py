class Card:
    def __init__(self, rank, suit, modifier):
        self.rank = rank
        self.suit = suit
        self.modifier = modifier

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

print(deck)

#list = [[1, 'h', 'none'], [2, 'h', 'none'], [3, 'h', 'none'], [4, 'h', 'none'], [5, 'h', 'none'], [6, 'h', 'none'], [7, 'h', 'none'], [8, 'h', 'none'], [9, 'h', 'none'], [10, 'h', 'none'], [11, 'h', 'none'], [12, 'h', 'none'], [13, 'h', 'none'], [1, 's', 'none'], [2, 's', 'none'], [3, 's', 'none'], [4, 's', 'none'], [5, 's', 'none'], [6, 's', 'none'], [7, 's', 'none'], [8, 's', 'none'], [9, 's', 'none'], [10, 's', 'none'], [11, 's', 'none'], [12, 's', 'none'], [13, 's', 'none'], [1, 's', 'none'], [2, 's', 'none'], [3, 's', 'none'], [4, 's', 'none'], [5, 's', 'none'], [6, 's', 'none'], [7, 's', 'none'], [8, 's', 'none'], [9, 's', 'none'], [10, 's', 'none'], [11, 's', 'none'], [12, 's', 'none'], [13, 's', 'none'], [1, 'c', 'none'], [2, 'c', 'none'], [3, 'c', 'none'], [4, 'c', 'none'], [5, 'c', 'none'], [6, 'c', 'none'], [7, 'c', 'none'], [8, 'c', 'none'], [9, 'c', 'none'], [10, 'c', 'none'], [11, 'c', 'none'], [12, 'c', 'none'], [13, 'c', 'none']]
#for i in range(52):
        #print(f"list.append(Card{tuple(list[i])})")
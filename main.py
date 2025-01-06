import os
import random

#Classes
#region

class Card:
    def __init__(self, rank, suit, modifier, ind):
        self.ID = ind
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
            image.append("|  qp  |")
            image.append("|  qp  |")
        return image
    
    def card_to_ascii(self):
        image = ["--------"]
        if self.modifier != "wild":
            if self.rank < 10 and self.rank > 1:
                image.append(f"|{self.rank}     |")
                image = self.suit_to_ascii(image)
                image.append(f"|     {self.rank}|")
            elif self.rank ==10:
                image.append(f"|{self.rank}    |")
                image = self.suit_to_ascii(image)
                image.append(f"|    {self.rank}|")                
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
        
        self.cards = cards

    @property
    def length(self):
        return len(self.cards)

    def sort(self, mode):
        if mode == "s":
            self.cards.sort(key=lambda card: card.rank)
            self.cards.sort(key=lambda card: card.suit)
        if mode == "r":
            self.cards.sort(key=lambda card: card.suit)
            self.cards.sort(key=lambda card: card.rank)

    def __str__(self):
        strng = ""
        for i in self.cards:
            strng += str(i) + " "
        return strng

    def shuffle(self):
        random.shuffle(self.cards)
        
class Hand(Deck):

    def __init__(self, cards, sorting):
        super().__init__(cards)
        self.sorting = sorting
        self.sort(self.sorting)

    def sort(self, mode):
        super().sort(mode)
        self.sorting = mode

    def play(self, max, score):
        valid = [False]

        #get choice
        while not all(valid):
            valid = []
            output = []
            print_hand(self, score)
            play = input("\nWhich cards would you like to play? Seperate them with a space. Enter 's' to change the sorting: ")
            os.system('clear')

            #change sorting
            if play == "s":
                valid.append(False)
                if self.sorting == "r":
                    self.sorting = "s"
                else:
                    self.sorting = "r"
                self.sort(self.sorting)
            
            #check if play is valid
            else:
                play = play.split(" ")
                if len(play) > max:
                    valid.append(False)
                else:
                    for card in play:
                        if card.isnumeric():
                            if int(card) -1 in range(self.length):
                                valid.append(True)
                                output.append(int(card)-1)
                            else:
                                print("That is an invalid input")
                                valid.append(False)
                        else:
                            print("That is an invalid input")
                            valid.append(False)
        
        return output

#endregion
   
#Functions
#region
def print_hand(printed, score):
    art = []
    for i in range(printed.length): #for every card in hand
        art.append(printed.cards[i].card_to_ascii()) #add an image of that card

    for i in range(6):
        line = ""
        for j in range(printed.length):
            line += art[j][i]
            if j + 1 != printed.length:
                line += "   "
        print(line)
    
    for i in range(printed.length):
        print(f"  {i+1}  {i+1}  ", end="   ")
    print(f"\nScore: {score}")

def create_random_card(ind):
    suit = random.choice(["h","c","d","s"])
    rank = random.randint(0,13)
    modifier = random.choice("none","none","none","none","none","none","none","none","none","wild")
    ind += 1
    return rank, suit, modifier, ind

def draw(deck, hand, amount, max):
    if hand.length + amount > max:
        amount = max - hand.length
    for i in range(amount):
        card = deck.cards.pop(0)
        hand.cards.append(card)
    return hand.cards, deck.cards

def is_flush(hand):
    for i in range(hand.length - 1):
        if hand.cards[i].suit != hand.cards[hand.length].suit:
            return False
    return True

def score_hand(hand, score, levels: dict):
    chips = 0
    ishand = True
    play = ""
    # if hand.length == 5:
    #     hand.sort("r")
    #     for i in range(4):
    #         if hand.cards[i+1].rank != hand.cards[0].rank:
    #             ishand = False
    #     if ishand:
    #         if is_flush(hand):
    #             chips = (hand.cards[0].rank * 5) + (((levels[flush_five] - 1) * 0.02) + 1) * levels


#endregion

#Variables
#region

#Create Starting Deck
#region
list = []
list.append(Card(1, 'h', 'none', 1))
list.append(Card(2, 'h', 'none', 2))
list.append(Card(3, 'h', 'none', 3))
list.append(Card(4, 'h', 'none', 4))
list.append(Card(5, 'h', 'none', 5))
list.append(Card(6, 'h', 'none', 6))
list.append(Card(7, 'h', 'none', 7))
list.append(Card(8, 'h', 'none', 8))
list.append(Card(9, 'h', 'none', 9))
list.append(Card(10, 'h', 'none', 10))
list.append(Card(11, 'h', 'none', 11))
list.append(Card(12, 'h', 'none', 12))
list.append(Card(13, 'h', 'none', 13))
list.append(Card(1, 'd', 'none', 14))
list.append(Card(2, 'd', 'none', 15))
list.append(Card(3, 'd', 'none', 16))
list.append(Card(4, 'd', 'none', 17))
list.append(Card(5, 'd', 'none', 18))
list.append(Card(6, 'd', 'none', 19))
list.append(Card(7, 'd', 'none', 20))
list.append(Card(8, 'd', 'none', 21))
list.append(Card(9, 'd', 'none', 22))
list.append(Card(10, 'd', 'none', 23))
list.append(Card(11, 'd', 'none', 24))
list.append(Card(12, 'd', 'none', 25))
list.append(Card(13, 'd', 'none', 26))
list.append(Card(1, 's', 'none', 27))
list.append(Card(2, 's', 'none', 28))
list.append(Card(3, 's', 'none', 29))
list.append(Card(4, 's', 'none', 30))
list.append(Card(5, 's', 'none', 31))
list.append(Card(6, 's', 'none', 32))
list.append(Card(7, 's', 'none', 33))
list.append(Card(8, 's', 'none', 34))
list.append(Card(9, 's', 'none', 35))
list.append(Card(10, 's', 'none', 36))
list.append(Card(11, 's', 'none', 37))
list.append(Card(12, 's', 'none', 38))
list.append(Card(13, 's', 'none', 39))
list.append(Card(1, 'c', 'none', 40))
list.append(Card(2, 'c', 'none', 41))
list.append(Card(3, 'c', 'none', 42))
list.append(Card(4, 'c', 'none', 43))
list.append(Card(5, 'c', 'none', 44))
list.append(Card(6, 'c', 'none', 45))
list.append(Card(7, 'c', 'none', 46))
list.append(Card(8, 'c', 'none', 47))
list.append(Card(9, 'c', 'none', 48))
list.append(Card(10, 'c', 'none', 49))
list.append(Card(11, 'c', 'none', 50))
list.append(Card(12, 'c', 'none', 51))
list.append(Card(13, 'c', 'none', 52))
deck = Deck(list)
deck.sort("s")
#endregion

hand = Hand([], "r")
ID = 52

played = Deck([])

discard = Deck([])

p_hands = {"flush_five":[40,7], "flush_house":[35,6], "five":[30,6], "royal_flush":[30,5], "flush_straight":[20,5], "four":[20,4], "house":[15,4], "flush_":[10,4], "straight":[5,4], "three":[30,3], "two_pair":[20,2], "pair":[0,2], "high":[0,1]}

cards = 52
hand_size = 7
play_size = 5
draw_size = 7
score = 0
target = 0
playing = True
inGame = True
inShop = False
#endregion

#Game loop
#region

os.system('clear')
print("HELLO THERE\nWelcome to POKER GAME tm\nTutorial in README")
input("\n\nPress ENTER to begin game")

while playing:
    
    if inGame:
        deck.shuffle()
        score = 0
        os.system('clear')
    while inGame:

        hand.cards, deck.cards = draw(deck, hand, draw_size, hand_size)
        hand.sort(hand.sorting)

        playedID = hand.play(play_size, score)
        step = 0
        for i in playedID:
            played.cards.append(hand.cards[i])
        for i in playedID:
            hand.cards.pop(i-step)
            step += 1
        step = 0

        score_hand(played, score, p_hands)
        print("PLAYED:")
        print_hand(played, score)

        draw_size = played.length
        draw(played, discard, draw_size, cards)
        if score >= target:
        inGame = False


#endregion
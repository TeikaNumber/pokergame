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
            elif self.rank == 14:
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
    
    def score(self, chips, mult):
        if self.rank < 11:
            chips += self.rank
        elif self.rank != 14:
            chips += 10
        else:
            chips += 11
        if self.modifier == "mult2":
            mult += 2
        elif self.modifier == "mult4":
            mult += 4
        elif self.modifier == "holo":
            mult *= 2
        elif self.modifier == "plus2":
            chips += 2
        elif self.modifier == "plus4":
            chips += 4
        elif self.modifier == "foil":
            chips *= 2

        return chips, mult

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

class Shop(Deck):
    def __init__(self, cards, price):
        super().__init__(cards)
        self.price = price
        self.reroll = 3

    def buy(self, money):
        print(f"Each card currently costs ${self.price}")
        play = input("Would you like to buy a card (b), reroll(r), or continue to the next round(c)? ")
        if play == "b":
            sale = input("Which card would you like to buy? (Please input numerically): ")
            return True, int(sale) - 1, money
        elif play == "r":
            if money >= self.reroll:
                money -= self.reroll
                self.reroll += 1
            return True, 99, money
        else:
            return False, 99, money


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
            play = input("\nWhich cards would you like to select? Seperate them with a space. Enter 's' to change the sorting: ")
            os.system('cls')

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
    if score != "":
        print(f"\nScore: {score}")
    else:
        print("\n")

def create_random_card(ind):
    suit = random.choice(["h","c","d","s"])
    rank = random.randint(0,13)
    modifier = random.choice(["none","none","none","none","none","none","none","none","none","wild"])
    ind += 1
    return Card(rank, suit, modifier, ind)

def draw(deck: Deck, hand: Deck, amount, max):
    if hand.length + amount > max:
        amount = max - hand.length
    for i in range(amount):
        card = deck.cards.pop(0)
        hand.cards.append(card)
    return hand.cards, deck.cards

def is_flush(hand, cards):
    if hand.length != 5:
        return False, cards
    for i in range(4):
        if hand.cards[i].suit != hand.cards[4].suit:
            return False, cards
    return True, [0,1,2,3,4]

def is_five(hand, cards):
    if hand.length != 5:
        return False, cards
    for i in range(4):
        if hand.cards[i].rank != hand.cards[4].rank:
            return False, cards
    return True, hand.cards

def is_four(hand, cards):
    count = []
    target = 4
    counted_cards = []
    if hand.length < target:
        return False, cards
    for i in range(hand.length):
        count.append(0)
        counted_cards.append([])
        for j in range(hand.length):
            if hand.cards[i].rank == hand.cards[j].rank:
                count[i] += 1
                counted_cards[i].append(j)
    if target in count:
        solution = count.index(target)
        return True, counted_cards[solution]
    return False, cards
                
def is_three(hand, cards):
    count = []
    target = 3
    counted_cards = []
    if hand.length < target:
        return False, cards
    for i in range(hand.length):
        count.append(0)
        counted_cards.append([])
        for j in range(hand.length):
            if hand.cards[i].rank == hand.cards[j].rank:
                count[i] += 1
                counted_cards[i].append(j)
    if target in count:
        solution = count.index(target)
        return True, counted_cards[solution]
    return False, cards

def is_pair(hand, cards):
    count = []
    target = 2
    counted_cards = []
    if hand.length < target:
        return False, cards
    for i in range(hand.length):
        count.append(0)
        counted_cards.append([])
        for j in range(hand.length):
            if hand.cards[i].rank == hand.cards[j].rank:
                count[i] += 1
                counted_cards[i].append(j)
    if target in count:
        solution = count.index(target)
        return True, counted_cards[solution]
    return False, cards

def is_straight(hand, cards):
    straight = Deck([])
    if hand.length != 5:
        return False, cards
    for i in range(5):
        straight.cards.append(hand.cards[i])
    straight.sort('r')
    for i in range(1,5):
        if straight.cards[i].rank - straight.cards[i-1].rank != 1:
            return False, cards
    return True, [0,1,2,3,4]

def is_two_pair(hand, cards):
    output = []
    hold = []
    hand.sort("r")
    ishand, output = is_pair(hand, output)
    if ishand:
        step = 0
        for i in range(2):
            x = hand.cards.pop(output[i-step])
            hold.append(x)
            step += 1
        step = 0
        ishand, card = is_pair(hand, output)
        for i in hold:
            hand.cards.insert(0,i)
        for i in range(len(card)):
            output.append(card.pop(0))
        if ishand:
            output[2] += 2
            output[3] += 2
            return True, output
    return False, cards

def score_hand(hand, score, levels: dict):

    #Variables
    #region
    chips = 0
    multiplier = 0
    cards = []
    play = "none"
    #endregion

    #Find hand
    #region
    ishand, cards = is_five(hand, cards)
    if ishand:
        ishand, cards = is_flush(hand,cards)
        if ishand:
            play = "flush_five"
        else:
            play = "five"
    ishand, cards = is_four(hand,cards)
    if ishand:
        play = "four"
    ishand, cards = is_three(hand,cards)
    if ishand:
        play = "three"
        ishand, cards = is_pair(hand,cards)
        if ishand:
            play = "house"
            ishand, cards = is_flush(hand, cards)
            if ishand:
                play = "flush_house"
    ishand, cards = is_pair(hand,cards)
    if ishand:
        play = "pair"
        ishand, cards = is_three(hand,cards)
        if ishand:
            play = "house"
            ishand, cards = is_flush(hand, cards)
            if ishand:
                play = "flush_house"
    ishand, cards = is_straight(hand, cards)
    if ishand:
        play = "straight"
        ishand, cards = is_flush(hand, cards)
        if ishand:
            count = 0
            play = "flush_straight"
            for i in range(5):
                if hand.cards[i].rank == 10 or hand.cards[i].rank == 14:
                    count += 1
            if count == 2:
                play = 'royal_flush'
            count = 0
    ishand, cards = is_two_pair(hand, cards)
    if ishand:
        play = "two_pair"
    ishand, cards = is_flush(hand, cards)
    if ishand:
        if play not in "flush_five flush_house flush_straight royal_flush":
            play = "flush"
    if cards == []:
        play = "high"
        hand.sort("r")
        cards.append(-1)
    #endregion

    #Calculate score
    #region
    x = levels[play]
    chips += x[0]
    multiplier += x[1]
    for i in cards:
        chips, multiplier = hand.cards[i].score(chips, multiplier)
    score += (chips * multiplier)
    #endregion
    
    return score

#endregion

#Variables
#region

#Create Starting Deck
#region
list = []
list.append(Card(14, 'h', 'none', 1))
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
list.append(Card(14, 'd', 'none', 14))
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
list.append(Card(14, 's', 'none', 27))
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
list.append(Card(14, 'c', 'none', 40))
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
shop = Shop([], 2)
discard = Deck([])

p_hands = {"flush_five":[40,7], "flush_house":[35,6], "five":[30,6], "royal_flush":[30,5], "flush_straight":[20,5], "four":[20,4], "house":[15,4], "flush":[10,4], "straight":[5,4], "three":[30,3], "two_pair":[20,2], "pair":[0,2], "high":[0,1]}

total_cards = 52
shop_price = 2
cash = 0
shop_size = 3
hand_size = 7
play_size = 5
draw_size = 7
score = 0
target = 50
base_discards = 3
base_hands = 4
playing = True
inGame = True
inShop = False
#endregion

#Game loop
#region

os.system('cls')
print("HELLO THERE\nWelcome to POKER GAME tm\nTutorial in README")
input("\n\nPress ENTER to begin game")

while playing:
    
    if inGame:
        deck.shuffle()
        score = 0
        os.system('cls')
        discards = base_discards
        hands = base_hands
    while inGame:
        os.system('clear' if os == 'NT' else 'cls')
        hand.cards, deck.cards = draw(deck, hand, draw_size, hand_size)
        hand.sort(hand.sorting)
        play = "n"
        while play != "p":
            hand.sort(hand.sorting)
            playedID = hand.play(play_size, score)
            step = 0
            for i in playedID:
                played.cards.append(hand.cards[i])
            print_hand(played, "")
            play = input(f"Would like to play, discard, or niether? (p ({hands} remaining), d ({discards} remaining), n): ")
            os.system('cls')
            if play == "p":
                if hands != 0:
                    for i in playedID:
                        hand.cards.pop(i-step)
                        step += 1
                        hands -= 1
                else:
                    play = "n"
                
            elif play == "d":
                if discards != 0:
                    for i in playedID:
                        hand.cards.pop(i-step)
                        step += 1
                    draw_size = played.length
                    discard.cards, played.cards = draw(played, discard, draw_size, total_cards)
                    hand.cards, deck.cards = draw(deck, hand, draw_size, total_cards)
                    discards -= 1
                else:
                    play = "n"
            if play == "n":
                played.cards = []
            step = 0

        score = score_hand(played, score, p_hands)
        print("PLAYED:")
        print_hand(played, score)
        input("Press ENTER to continue:")
        draw_size = played.length
        discard.cards, played.cards = draw(played, discard, draw_size, total_cards)
        if score >= target:
            inGame = False
            deck.cards, hand.cards = draw(deck, hand, draw_size, total_cards)
            deck.cards, discard.cards = draw(deck, discard, draw_size, total_cards)
            inShop = True
            input("\n\nCongrats, you beat this level! Press ENTER to continue: ")
        if hands == 0 and inGame:
            inGame = False
            playing = False

    while inShop:
        for i in range(shop_size):
            ID += 1
            x = create_random_card(ID)
            shop.cards.append(x)
        print_hand(shop, "")
        inShop, x, cash = shop.buy(cash)
        if x != 99:
            deck.cards.append(shop.cards[x-1])
            
print("Game Over")


#endregion
# Blackjack Game

"""
Once game starts, two cards each are dealt to the two players (dealer and player).
if game is in play and player clicks the deal button, they loose. 
The first card of the dealer (called the hole) is faced down while game is in play. its revealed once there is a winner
While the game is ongoing, clicking the hit button gives the player an extra card.
if the total value of players cards exceeds 21 after being 'hit', player is busted(losses).
if player chooses to stand, dealer is hit repeatedly until hand has value 17 or more,
then values for player and dealer calculated. lower value losses.
"""

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score_counter = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos, hole=False):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))   
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    """class shares cards to players"""
    def __init__(self):
        """players start out with no cards"""
        self.cards = []           

    def __str__(self):
        """returns the string representation of cards shared"""
        return "Hand contains " + " ".join([str(i) for i in self.cards])

    def add_card(self, card):
        self.cards.append(card)  # adds card to a players collection

    def get_value(self):
        """function calculates the value of individual's card
        
        cards are looped over and summed based on the VALUES dict above.
        if total value < 12, and a player had at least one ace (A),
        they can add an extra 10 to their value since aces have values of
        either 1 or 11. This brings their total value up, yet keeps it < 22"""
    
        value = 0
        check = []
        for i in self.cards:
            card_rank = i.get_rank()
            check.append(card_rank)
            for key, val in VALUES.items():
                if card_rank == key:
                    value += val
        if value < 12 and 'A' in check:
            value += 10
        return value
   
    def draw(self, canvas, pos):
        """draw a hand on the canvas, use the draw method for cards"""
        
        for i in self.cards:           
            i.draw(canvas, pos)
            pos[1] += 20
 
        
# define deck class 
class Deck:
    """class creates a deck of card. a deck contains 52 cards of suits and ranks"""
    def __init__(self):
        self.deck = []	
        for suit in SUITS:
            for rank in RANKS:
                one_card = Card(suit,rank)
                self.deck.append(one_card)

    def shuffle(self):
        # function shuffles the deck 
        random.shuffle(self.deck)   # use random.shuffle()

    def deal_card(self):
        # function shares cards to players. The top most card is given out
        return self.deck.pop()
    
    def __str__(self):
        """function returns the string representation of the games's deck of cards"""
        return 'Deck contains ' + ' '.join([str(i) for i in self.deck]) 


#define event handlers for buttons
def deal():
    """game starts. deal function shuffles the deck and deals two
    cards each to the two players (dealer and player). if game is in play
    and player clicks the deal button, they loose"""
    
    global outcome, in_play, player, dealer, game_deck, score_counter
    
    if in_play:
        outcome = "You ended game! You lost!! Play again?"
        score_counter -= 1
        in_play = False
    else:            
        game_deck = Deck()
        game_deck.shuffle()

        player = Hand()
        dealer = Hand()

        #gives two cards each to player and dealer, and prints their card numbers
        i = 0
        while i < 2:
            player.add_card(game_deck.deal_card())
            dealer.add_card(game_deck.deal_card())
            i += 1
        #print 'player - ', player
        #print 'dealer - ', dealer

        in_play = True
        outcome = "Hit or Stand?"
            
def hit():
    """While the game is ongoing, clicking the hit button gives the player an extra card
    if the total value of players cards exceeds 21 after being 'hit', player is busted(losses)"""
    
    global score_counter, outcome, in_play
    
    if in_play:
        player.add_card(game_deck.deal_card())
        if Hand.get_value(player) > 21:
            outcome = "You busted! You lost!! Deal again?"
            score_counter -= 1
            in_play = False
            return score_counter 
        
def stand():
    """if player chooses to stand, dealer is hit repeatedly until hand has value 17
    or more"""
    global in_play, score_counter, outcome
    
    if in_play:
        while Hand.get_value(dealer) < 17:
            dealer.add_card(game_deck.deal_card())
        if Hand.get_value(dealer) > 21:
            outcome = "dealer busted! You won!! New Deal?"
            score_counter += 1
            in_play = False
            return score_counter
        else:
            if Hand.get_value(player) <= Hand.get_value(dealer):
                outcome = "Lower total! You lost!! Deal again?"
                score_counter -= 1
                in_play = False
                return score_counter
            else:
                #print "dealer score lower, player wins!!! Game Over"
                outcome = "Higher total! You won!! New Deal?"
                score_counter += 1
                in_play = False
                return score_counter 

# draw handler    
def draw(canvas):
    """function draws the player and dealer cards on the canvas, alongside
    other game parameters. The first card of the dealer (called the hole) is
    faced down while game is in play. its revealed once there is a winner"""
    
    player.draw(canvas, [95, 125])
    dealer.draw(canvas, [446, 126])
    canvas.draw_text('Blackjack', (200, 50), 50, 'Green')
    canvas.draw_text('player', (100, 100), 27, 'Black')
    canvas.draw_text('dealer', (450, 100), 27, 'Black')
    canvas.draw_text(outcome, (148, 380), 28, 'Black')
    canvas.draw_text('Player score:', (50, 500), 27, 'Black')
    canvas.draw_text(str(score_counter), (200, 500), 27, 'Green')
    
    #if game is in play, dealers first card is faced down
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, (72, 19), [446 +  CARD_BACK_CENTER[0], 136], (72, 19))
        
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Grey")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()



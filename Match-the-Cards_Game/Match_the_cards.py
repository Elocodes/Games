# implementation of card game - Memory

"""
This module contains a card game where the player has to open two cards that
bear the same number. Players aim to use the least amount of turns possible
to match all the cards. Memorizing the number of each card previously exposed
is key to matching numbers fast. 
"""

import simplegui
import random

card_list = []
new_list = []
exposed = []

for i in range(8):
    to_str = str(i)
    card_list.append(to_str)
    new_list.append(to_str)
   
card_list.extend(new_list)

for i in range(len(card_list)):
        exposed.append(False)

# helper function to initialize globals
def new_game():
    """function shuffles the card, turns the back of all cards (that is,
    exposed returns to false, and starts a new game"""
    
    global game_state, turn, exposed, card_list 
    
    random.shuffle(card_list)
    game_state = 0
    turn = 0
    label.set_text('Turns =  ' + str(turn))
    for i in range(len(card_list)):
        exposed[i] = False
         
# define event handlers
def mouseclick(pos):  
    """
    function determines which position the mouse clicked by dividing the x position
    of the mouse by the width of the card. this gives integer numbers, 0, 1,
    etc up to 15. in this way each card is accounted for. since pos is a tuple,
    change to list first for iteration
    
    first click - game state is 1, second click - game state 2. if the two cards exposed
    are not the same number, the next click takes the game bck to state 1. At the end of
    the two states, the player has played one turn
    """
    
    global cardnum_clicked, game_state, card1, card2, turn
    
    click_pos = list(pos)
    cardnum_clicked = click_pos[0] // 50
        
    if game_state == 0:
        if exposed[cardnum_clicked] == False:
            card1 = cardnum_clicked
            exposed[card1] = True
            game_state = 1
            turn += 1
    
    elif game_state == 1:
        if exposed[cardnum_clicked] == False:            
            card2 = cardnum_clicked
            exposed[card2] = True
            game_state = 2
            
    elif game_state == 2:
        if card_list[card1] != card_list[card2]:
            exposed[card1] = False
            exposed[card2] = False
        if exposed[cardnum_clicked] == False:  
            card1 = cardnum_clicked
            exposed[card1] = True
            turn += 1
            game_state = 1
            
    label.set_text('Turns =  ' + str(turn))
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    """function divides the canvas into 16 rectangles representing
    cards, and inserts the numbers in the card list on them"""
        
    # Draw each card as a polygon. The list from left to right are: lower left, upper left, upper right, lower right
    # if a card is exposed, then draw(show) its text
    for i in range(len(card_list)):
        if exposed[i] == True:
            card_center = [25 + (i * 50), 50]                                                        
            canvas.draw_text(card_list[i], card_center, 35, 'White')
        else:
            canvas.draw_polygon([[50*i, 100], [50*i, 0], [50*(i+1), 0], [50*(i+1), 100]], 1, 'Black', 'Green')
            
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
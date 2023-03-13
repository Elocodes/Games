# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui
import math

num_range = 100
num_of_guesses_allowed = int(math.log(num_range,2)) + 1
secret_number = random.randrange(0,num_range)

# helper function to start and restart the game
def new_game():
    """Computes the guesses and gets the secret number"""
    global num_range
    
    global num_of_guesses_allowed 
    num_of_guesses_allowed = int(math.log(num_range,2)) + 1
    
    global secret_number  
    secret_number = random.randrange(0,num_range)
    
    print "New game. Range is from 0 to", num_range
    
    print "Number of remaining guesses is", num_of_guesses_allowed
    
    print
        
# define event handlers for control panel
def range100():
    """ button that changes the range to [0,100) and starts a new game"""
    
    global num_range          #since the num_range is already 100 above, this loacalizes it for this function
    num_range = 100
    
    global num_of_guesses_allowed
    num_of_guesses_allowed = int(math.log(num_range,2)) + 1
    
    new_game()                #calls on a new game game to start whenever the range100 button is clicked
      

def range1000():
    """ button that changes the range to [0,1000) and starts a new game"""     
    
    global num_range
    num_range = 1000
            
    global num_of_guesses_allowed
    num_of_guesses_allowed = int(math.log(num_range,2)) + 1
    
    new_game()
    
def input_guess(guess):
    """ main game logic goes here"""
    
    player_guess = int(guess)           #gets player's guess    
    print "Guess was", player_guess
    
    global secret_number
    
    global num_of_guesses_allowed
    num_of_guesses_allowed -= 1           #countsdown on the number of guesses allowed
     
    if num_of_guesses_allowed > 0:
        print "Number of remaining guesses is", num_of_guesses_allowed    
        if player_guess > secret_number:
            print "lower!"
        elif player_guess < secret_number:
            print "higher!"
        else:
            print "correct!"
            print
            new_game()   
    
    if num_of_guesses_allowed == 0:
        print "Number of remaining guesses is", num_of_guesses_allowed
        if player_guess == secret_number:
            print "Correct!"
            print
            new_game()
        else:
            print "You ran out of guesses. The number was", secret_number
            print
            
            new_game()
            
    print
        
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
f.add_button("Range is [0,100)", range100, 200)
f.add_button("Range is [0,1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)

# start frame
f.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric

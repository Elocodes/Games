# GUI-based version of RPSLS

# This program runs the popular game of rock paper scissors between a user
# and the computer. Based on the input of the user, it displays if the user
# or the computer wins, or if a tie.  

import simplegui
import random

def name_to_number(name):
    ''' Assigning numbers from 0 to 4 to the RPSLS'''
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Error: name does not match game"
        
    # convert name to number using if/elif/else
    # don't forget to return the result!

def number_to_name(number):
    ''' Assigning numbers from 0 to 4 to the RPSLS'''
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "Error: number is not in the correct range"
    
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    
   # print out the message for the player's choice
    
    print "Player chooses", player_choice
    
    # convert the player's choice to player_number using the function name_to_number()
    
    player_number = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    
    computers_number = random.randrange(0,5)
    
    # convert comp_number to comp_choice using the function number_to_name()
    
    computers_choice = number_to_name(computers_number)
    
    # print out the message for computer's choice
    
    print "computer choses", computers_choice

    # compute difference of comp_number and player_number modulo five
    
    comparison_benchmark = (player_number - computers_number) 

    # use if/elif/else to determine winner, print winner message

        
    if comparison_benchmark % 5 == 0:
        print "Player and Computer tie!"
    
    elif 2 < (comparison_benchmark % 5) < 5:
        print "Computer wins!"
    
    elif 0 < (comparison_benchmark % 5) < 3: 
        print "Player wins!"
    
    else:
        print "Error: game invalid"
    
    # print a blank line to separate consecutive games
    print

# handler for input field
def get_guess(guess):
    
    # validate input
    if not (guess == "rock" or guess == "Spock" or guess == "paper" or
            guess == "lizard" or guess == "scissors"):
        print 'Error: Bad input "' + guess + '" to rpsls'
        
        print
        
    else:
        rpsls(guess)
    

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_input("Enter guess for RPSLS", get_guess, 200)


# Start the frame animation
frame.start()


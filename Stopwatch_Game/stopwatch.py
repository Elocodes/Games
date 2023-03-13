# Program for "Stopwatch: The Game"

import simplegui

# define global variables

current_time = 0
num_of_stop_button_clicks = 0
num_of_game_wins = 0
increment_scores = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format():
    global current_time, game_check,num_of_game_wins
    t = current_time
    A = (t // 600)               # gets the minutes from the tenth of seconds by first dividing the tenths of seconds by 10 and then dividing further by 60
    B = ((t // 10) % 60) // 10   # taking the remainder from A which gives the seconds and dividing by 10 to get the tens of seconds 
    C = ((t // 10) % 60) % 10    # remainder from th etens of seconds 
    D = (t % 10)                 # recall that the curent time is in tenths of seconds. taking its remainder gives us the numers that is less than one full second        
    return str(A) + ":" + str(B) + str(C) + "." + str(D)

# define event handlers for buttons; "Start", "Stop", "Reset"
def stopwatch_start():
    global total_clicks, increment_scores  
    timer.start()
    Not_running = False
    increment_scores = False
    
def stopwatch_stop():
    global num_of_stop_button_clicks, num_of_game_wins, current_time, increment_scores 
    timer.stop()
    Not_running = True
    if (Not_running == True) and (increment_scores == False):
        num_of_stop_button_clicks +=1              # for the game aspect, this captures the number of times the stop button was clicked
        if (current_time % 10) == 0:
            num_of_game_wins +=1                   #captures the number of game wins at whole seconds(1.0,2.0 etc)         
        increment_scores = True                    #increment_scores only become false when the start watch button is pressed. so by calling its True version at this point, ensures stop can only run again when start must have been run 
            
def stopwatch_restart():
    global current_time, num_of_stop_button_clicks, num_of_game_wins
    current_time = 0
    num_of_stop_button_clicks = 0
    num_of_game_wins = 0
    
# define event handler for timer with 0.1 sec interval
def tick():
    global current_time
    current_time += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(str(format()), (75, 100), 30, "White")
    canvas.draw_text(str(num_of_stop_button_clicks), (170, 30), 15, "White")
    canvas.draw_line((162, 33), (165, 17), 2, "White")
    canvas.draw_text(str(num_of_game_wins), (150, 30), 15, "White")
        
# create frame
frame = simplegui.create_frame("Stopwatch", 200, 200)

# register event handlers
timer = simplegui.create_timer(100, tick)
frame.set_draw_handler(draw)
frame.add_button("Start", stopwatch_start)
frame.add_button("Stop", stopwatch_stop)
frame.add_button("Reset", stopwatch_restart)

# start frame
frame.start()

# Please remember to review the grading rubric

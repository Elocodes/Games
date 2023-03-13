# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True


ball_pos =[WIDTH / 2, HEIGHT / 2]
ball_vel =[240/60.0, 240.0/60.0]                                 #ball movement in pixels per seconds

increase = [1.1]

paddle1_pos = (HEIGHT/2) - (PAD_HEIGHT / 2)                      # The vertical point(the y point) of my line. coined from paddle1_x,y axes = ([0,(HEIGHT/2) - (PAD_HEIGHT / 2)], [PAD_WIDTH, (HEIGHT/2) - (PAD_HEIGHT / 2)] ). To be called in the draw handler

paddle1_vel = 0

paddle2_pos = (HEIGHT/2) - (PAD_HEIGHT / 2)
paddle2_vel = 0

score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left

def spawn_ball(direction):
    global ball_pos, ball_vel, BALL_RADIUS # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == RIGHT:
        ball_vel = [random.randrange(120, 240)/ 60.0, -random.randrange(60, 180)/ 60.0]
    if direction == LEFT:
        ball_vel = [-random.randrange(120, 240)/ 60.0, -random.randrange(60, 180)/ 60.0]
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    spawn_ball(LEFT)
    
def restart_button():
    new_game()

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel, increase
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0] 
    ball_pos[1] += ball_vel[1]
    
    if ball_pos[1] <= BALL_RADIUS:                                # to get the ball collide and bounce off the top and bottom respectively of the wall
        ball_vel[1] = -ball_vel[1]
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    
    if (ball_pos[0] <= PAD_WIDTH + BALL_RADIUS) and (ball_pos[1] >= paddle1_pos - PAD_HEIGHT) and (ball_pos[1] <= paddle1_pos + PAD_HEIGHT):  # code that satisfies this coditions; If the ball's X position has collided with the gutter, but the y position is "inside" the paddle's top and bottom (that means the ball touches the paddle), the ball should bounce fast to the center of the table, equivalent to when a player hits the ball hard in tennis
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] += increase[0]        
    elif (ball_pos[0] <= PAD_WIDTH + BALL_RADIUS) and (ball_pos[1] < paddle1_pos):                         #bounce back slowly if the ball hits above the paddle1
        score2 += 1
        spawn_ball(RIGHT)                                                                                  # adds score to player 2 each time the ball misses a paddle and hits the upper gutter 
    elif (ball_pos[0] <= PAD_WIDTH + BALL_RADIUS) and (ball_pos[1] > paddle1_pos + PAD_HEIGHT):            #boune back slowly if the ball hits below the paddle1                                           
        score2 += 1                                                                                        # adds score to player 2 each time the ball misses a paddle and hits the lower gutter
        spawn_ball(RIGHT)
        
    if (ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS) and (ball_pos[1] >= paddle2_pos - PAD_HEIGHT) and (ball_pos[1] <= paddle2_pos + PAD_HEIGHT):  # code that satisfies this coditions; If the ball's X position has collided with the gutter, but the y position is "inside" the paddle's top and bottom (that means the ball touches the paddle), the ball should bounce fast to the center of the table, equivalent to when a player hits the ball hard in tennis
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] += -increase[0]
    elif (ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS) and (ball_pos[1] < paddle2_pos):                         #bounce back slowly if the ball hits above the paddle2
        score1 += 1                                                                                                # adds score to player 1 each time the ball misses a paddle and hits the upper gutter
        spawn_ball(LEFT)
    elif (ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS) and (ball_pos[1] > paddle2_pos + PAD_HEIGHT):            #boune back slowly if the ball hits below the paddle2
        score1 += 1                                                                                                # adds score to player 1 each time the ball misses a paddle and hits the lower gutter
        spawn_ball(LEFT)
        
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 12, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += -paddle1_vel    
    if paddle1_pos <= PAD_HEIGHT / 2:
        paddle1_vel -= 2                                                   # to get the paddle1 collide and bounce off the top and bottom respectively of the wall
    if paddle1_pos == HEIGHT - (PAD_HEIGHT / 2):
        paddle1_vel += 2
        
    paddle2_pos += -paddle2_vel    
    if paddle2_pos <= PAD_HEIGHT / 2:
        paddle2_vel -= 2                                                   # to get the paddle2 collide and bounce off the top and bottom respectively of the wall
    if paddle2_pos == HEIGHT - (PAD_HEIGHT / 2):
        paddle2_vel += 2    
            
    # draw paddles
    canvas.draw_line((0, paddle1_pos), (PAD_WIDTH, paddle1_pos), 80, "White")
    canvas.draw_line((WIDTH - PAD_WIDTH, paddle2_pos), (WIDTH, paddle2_pos), 80, "White")
      
    # draw scores
    canvas.draw_text(str(score1), (150, 50), 40, "White")
    canvas.draw_text(str(score2), (450, 50), 40, "White")
     
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP['s']:       #keyboard key that takes paddle1 down by reducing the velocity when the s key is pressed down
        paddle1_vel = -2
        
    if key == simplegui.KEY_MAP['w']:       #keyboard key that takes paddle1 up by increasing the velocity when the w key is pressed down
        paddle1_vel = 2
        
    if key == simplegui.KEY_MAP['down']:    #keyboard key that takes paddle2 down by reducing the velocity when the down arrow key is pressed down
        paddle2_vel = -2    
        
    if key == simplegui.KEY_MAP['up']:      #keyboard key that takes paddle2 up by increasing the velocity when the up arrow key is pressed down
        paddle2_vel = 2 
        
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP['s']:       #keyboard key that stops paddle1 on its way down by making the velocity constant (0) when the s key is released (this is what is meant by keyup)
        paddle1_vel = 0
        
    if key == simplegui.KEY_MAP['w']:       #keyboard key that stops paddle1 on its way up by making the velocity constant (0) when the w key is released (this is what is meant by keyup)
        paddle1_vel = 0 
        
    if key == simplegui.KEY_MAP['down']:    #keyboard key that stops paddle2 on its way down by making the velocity constant (0) when the down arrow key is released (this is what is meant by keyup)
        paddle2_vel = 0
        
    if key == simplegui.KEY_MAP['up']:      #keyboard key that stops paddle2 on its way up by making the velocity constant (0) when the up arrow key is released (this is what is meant by keyup)
        paddle2_vel = 0    


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", restart_button, 70)


# start frame
new_game()
frame.start()

import turtle
import time
import random
snake=[[0,0],[-1,0],[-2,0],[-3,0]]
apple=[random.randint(-30,28),random.randint(-28,21)]
score=0
direction="Right"
gameover=False
delay=.05
counter=0
timer=10

def display():
    """
    Sig: () -> NoneType
    Draws a the snake body, apple, the score, and the boarder for
    the screen on the game.
    """
    global snake
    global apple
    global delay
    global counter
    
    turtle.hideturtle()

    #draws boarder in which would kill the snake
    turtle.color("black")
    turtle.penup()
    turtle.goto(-310,-250)
    turtle.down()
    for i in range(2):
        turtle.forward(600)
        turtle.left(90)
        turtle.forward(500)
        turtle.left(90)           

    #draw location of the snake
    turtle.penup()
    for body in snake:
        snakex=body[0]
        snakey=body[1]
        turtle.goto(snakex*10,snakey*10)
        turtle.down()
        
    #draw snake body
        turtle.color("green")
        turtle.begin_fill()
        for square in range(4):
            turtle.forward(10)
            turtle.right(90)         
        turtle.end_fill()
    
    #draw apple location
    turtle.penup()
    turtle.goto(apple[0]*10,apple[1]*10)
    turtle.down()

    #draw a red apple
    turtle.color("red")
    turtle.begin_fill()
    for appledraw in range(4):
        turtle.forward(10)
        turtle.right(90)   
    turtle.end_fill()
    turtle.color("blue")
    turtle.penup()
    turtle.goto(250,250)
    turtle.write(score, align="center", font=("Arial", 40, "normal"))
    turtle.down()
    time.sleep(delay)
    counter+=1

def myright():
    """
    Sig: () -> NoneType
    This function is responible for changing the location of the body when the
    snake is going in the right direction
    """
    global snake
    bodyx=snake[0][0]
    bodyy=snake[0][1]
    newx=bodyx+1
    snake=[[newx,bodyy]]+snake
    snake.pop()

def myleft():
    """
    Sig: () -> NoneType
    This function is responible for changing the location of the body when the
    snake is going in the left direction
    """
    global snake
    bodyx=snake[0][0]
    bodyy=snake[0][1]
    newx=bodyx-1
    snake=[[newx,bodyy]]+snake
    snake.pop()

def myup():
    """
    Sig: () -> NoneType
    This function is responible for changing the location of the body when the
    snake is going in the up direction
    """
    global snake
    bodyx=snake[0][0]
    bodyy=snake[0][1]
    newy=bodyy+1
    snake=[[bodyx,newy]]+snake
    snake.pop()

def mydown():
    """
    Sig: () -> NoneType
    This function is responible for changing the location of the body when the
    snake is going in the down direction
    """ 
    global snake
    bodyx=snake[0][0]
    bodyy=snake[0][1]
    newy=bodyy-1
    snake=[[bodyx,newy]]+snake
    snake.pop()

def Right_key():
    """
    Sig: () -> NoneType
    This function is responible giving direction the value of right when
    the right key is press and if the left key is pressed as it is in right
    key it will keep moving to the right 
    """
    global direction
    if direction!="Left":
        direction="Right"
def Left_key():
    """
    Sig: () -> NoneType
    This function is responible giving direction the value of left when
    the left key is press and if the right key is pressed as it is in left
    key it will keep moving to the left 
    """
    global direction
    if direction!="Right":
        direction="Left"
def Up_key():
    """
    Sig: () -> NoneType
    This function is responible giving direction the value of up when the
    up key is press and if the down key is pressed as it is in up key it
    will keep moving up 
    """
    global direction
    if direction!="Down":
        direction="Up"
def Down_key():
    """
    Sig: () -> NoneType
    This function is responible giving direction the value of down when the
    down key is press and if the up key is pressed as it is in down key it
    will keep moving up 
    """
    global direction
    if direction!="Up":
        direction="Down"
def physics():
    global direction
    global score
    global snake
    global gameover
    global counter
    global timer
    """
    Sig: () -> NoneType
    Here, in the function if direction is a particular direction it will go a
    corriponeding fuction to make the snake  move in the direction that was give. Here,
    it is not only moveing the snake contiunous but it is responsilbe for moving the
    apple each time the snake eats the apple.
    """
    
    if direction == "Right":
        myright()

    if direction == "Left":
        myleft()

    if direction == "Up":
        myup()

    if direction == "Down":
        mydown()

    # if the snake head goes over the apple the snake has eaten the apple
    if snake[0]== apple:
        apple.clear()
    # this will cause the apple position to change and make
        applex=random.randint(-31,28)
        appley=random.randint(-24,25)
        apple.append(applex)
        apple.append(appley)
    # the score will increase 
        score+=1
    #the snake will groaw
        snake.append(snake[-1])
    #the time counts down from the last time you ate the apple 
        counter=0
    #at a curtain time the apple moves(extra credit)
    if counter%(timer*10)==0:
        apple.clear()
        applex=random.randint(-31,28)
        appley=random.randint(-24,25)
        apple.append(applex)
        apple.append(appley)

        
def game():
    """
    Sig: () -> NoneType
    Here, if it is the gameover function in which if the snake was to go past the boarder
    or eat itself the game would be over.
    """
    global snake
    global gameover

    #this is for if the snake head goes over its own body it will die
    for i in range(len(snake)-1):
        if snake[0]==snake[1+i]:
            gameover=True

    #this is if the snake cross the boarder it will die
    for body in snake:
        snakex=body[0]
        snakey=body[1]
        if not -32<snakex<29 or not -25<snakey<26:
            gameover=True
    

def main():
    turtle.resizemode("user")
    turtle.tracer(0,0)
    turtle.speed(0.1)
    turtle.setup(640,600)
    
    while not gameover:
        turtle.clear()
        display()
        turtle.onkey(Right_key,"Right")
        turtle.onkey(Left_key,"Left")
        turtle.onkey(Up_key,"Up")
        turtle.onkey(Down_key,"Down")
        turtle.listen()
        turtle.update()
        physics()
        game()
    turtle.penup()
    turtle.goto(0,0)
    turtle.down()
    turtle.clear()
    turtle.write("Gameover", align="center", font=("Arial", 90, "normal"))
        
        
main()

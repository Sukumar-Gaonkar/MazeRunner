import turtle
import math


# PEN
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)

          

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)

    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor()+24
    
        if(move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            
    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor()-24
    
        if(move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()
    
        if(move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()
    
        if(move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)  

class Finish(turtle.Turtle):
     #def __init__(self, x, y):
     def __init__(self):
       turtle.Turtle.__init__(self)
       self.shape("square")
       self.color("red")
       self.penup()
       self.speed(0)
       #self.goto(x,y)
       

   # def destroy(self):
    #self.goto(2000,2000)
    #     self.hideturtle()
         
def setup_maze(level):
    wn = turtle.Screen()
    wn.bgcolor("light green")
    wn.title("A MAZE GAME")
    wn.setup(700,700)


    turtle.register_shape("wall.gif")

    #create class instances
    pen = Pen()
    player = Player()
    finish = Finish()

    #create wall list
    walls = []

    #finish = Finish()
    # print
    for y in range(len(level)):

        for x in range(len(level[y])):
            #GET CHARACTER AT EACH X,Y
            # NOTE THE ORDER OF X,Y
            character = level[y][x]

            #calculate x,y coordinates

            screen_x = -288+(x*24)
            screen_y = 288-(y*24)

            #check if it is an X(wall)
            if character == 1:
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))

            # check if it is a P
            if character == "P":
                player.goto(screen_x, screen_y)
            if character == "F":
                finish.goto(screen_x, screen_y)
                finish.stamp()

      


    
###########################################


# wn = turtle.Screen()
# wn.bgcolor("light green")
# wn.title("A MAZE GAME")
# wn.setup(700,700)
#
#
# turtle.register_shape("wall.gif")
#
# # CREATE LEVELS
#
# levels=[""]
#
# #FIRST LEVEL
#
# level_1 = [
#     "XXXXXXXXXXXXXXXXXXXXXXXXX",
#     "XP  XX           X   X XX",
#     "XXX    XXX    XXXXXXXXXXX",
#     "X     XXXXXX       XXXXXX",
#     "X      XXXXXXXX      XXXX",
#     "XXX  XXXXXXXX       XXXXX",
#     "XXXX        XXXX  XXXXXXX",
#     "X    XX      XXX    XXXXX",
#     "X XX      XXXX  XX    XXX",
#     "X XXX  XXXXXX  XXX   XXXX",
#     "XXXXXX         XXXXXXXXXX",
#     "X   XXXXX    X   XXXXXXXX",
#     "XXX      XXXXXX     XXXXX",
#     "XXXXXX             XXXXXX",
#     "XXXXXXXXX    XXXXXXXXXXXX",
#     "XXXXXXXXXXXX    XXXXXXXXX",
#     "XXXXXXXXXXXXXX    XXXXXXX",
#     "XXXXXXXXXXXXXXXXX    XXXX",
#     "XXXXXXXXXXXXXX    XXXXXXX",
#     "XXXXXXXXXX     XX  XXXXXX",
#     "XXXXXXXX    XXXXXX   XXXX",
#     "XXXXXXXXXXX   XXXXX   XXX",
#     "XXXXXXXXXXXXX          FX",
#     "XXXXXXXXXXXXXXXXXXXXXXXXX",
#     ]
#
# finishes=[]
# #ADD LEVEL
# levels.append(level_1)
# #level List[String] -> List[List[int]]
#
#
#
# #create class instances
# pen = Pen()
# player = Player()
# finish = Finish()
#
# #create wall list
# walls = []
#
# #finish = Finish()
#
# #SETUP LEVEL
# setup_maze(levels[1])
#
# #keyboard binding
# turtle.listen()
# turtle.onkey(player.go_left,"Left")
# turtle.onkey(player.go_right,"Right")
# turtle.onkey(player.go_up,"Up")
# turtle.onkey(player.go_down,"Down")
#
# #Turn off screen updates
# wn.tracer(0)
#
#
# #MAIN GAME LOOP
#
# while True:
#     if player.xcor() == finish.xcor() and player.ycor() == finish.ycor():
#        # wn.popup("path found")
#         print("PATH FOUND")
#
#
#     #update screen
#     wn.update()

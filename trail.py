import turtle
import math

wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("A MAZE GAME")
wn.setup(700,700)

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("green")
        self.penup()
        self.speed(0)

class Pencil(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("pink")
        self.penup()
        self.speed(0)         




levels=[""]

level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP  XX           X   X XX",
    "XXX    XXX    XXXXXXXXXXX",
    "X     XXXXXX       XXXXXX",
    "X      XXXXXXXX      XXXX",
    "XXX  XXXXXXXX       XXXXX",
    "XXXX        XXXX  XXXXXXX",
    "X    XX      XXX    XXXXX",
    "X XX      XXXX  XX    XXX",
    "X XXX  XXXXXX  XXX   XXXX",
    "XXXXXX         XXXXXXXXXX",
    "X   XXXXX    X   XXXXXXXX",
    "XXX      XXXXXX     XXXXX",
    "XXXXXX             XXXXXX",
    "XXXXXXXXX    XXXXXXXXXXXX",
    "XXXXXXXXXXXX    XXXXXXXXX",
    "XXXXXXXXXXXXXX    XXXXXXX",
    "XXXXXXXXXXXXXXXXX    XXXX",
    "XXXXXXXXXXXXXX    XXXXXXX",
    "XXXXXXXXXX     XX  XXXXXX",
    "XXXXXXXX    XXXXXX   XXXX",
    "XXXXXXXXXXX   XXXXX   XXX",
    "XXXXXXXXXXXXX          FX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    ]

levels.append(level_1)



def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            #GET CHARACTER AT EACH X,Y
            # NOTE THE ORDER OF X,Y
            character = level[y][x]

            #calculate x,y coordinates

            screen_x = -288+(x*24)
            screen_y = 288-(y*24)

            #check if it is an X(wall)
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))
          
paths = [""]

path_1 = [
    "SSSSDDDDWWWWAAAA",
    "",
    ]

paths.append(path_1)




def setup_path(path):
    screen_x = -288
    screen_y = 264

    for y in range(len(path)):
        for x in range(len(path[y])):
            #GET CHARACTER AT EACH X,Y
            # NOTE THE ORDER OF X,Y
            character = path[y][x]
            print(character)
        
            #left
            if character == "W":
                screen_x = screen_x-24
                screen_y = screen_y
                pencil.goto(screen_x , screen_y)
                pencil.stamp()
               
            #up    
            if character == "A":
                screen_x = screen_x
                screen_y = screen_y + 24
                pencil.goto(screen_x , screen_y )
                pencil.stamp()
                
            #right    
            if character == "S":
                screen_x = screen_x + 24
                screen_y = screen_y
                pencil.goto(screen_x  , screen_y )
                pencil.stamp()
                

            #down    
            if character == "D":
                screen_x = screen_x
                screen_y = screen_y - 24
                pencil.goto(screen_x , screen_y)
                pencil.stamp()
                


pen = Pen()
pencil = Pencil()
walls = []

setup_maze(levels[1])
setup_path(paths[1])

while True:
    pass
wn.tracer(0)

wn.update()

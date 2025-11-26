import turtle
import time

t = turtle.Turtle()
t.speed(10)
t.hideturtle()


# Letters

def a(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x+20, y+100)
    t.goto(x+40, y)
    t.penup()
    t.goto(x+10, y+50)
    t.pendown()
    t.goto(x+30, y+50)

def b(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x, y+100)
    t.goto(x+40, y+75)
    t.goto(x+5, y+50)
    t.goto(x+40, y+25)
    t.goto(x+40, y)
    t.goto(x, y)

def c(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x+40, y)
    t.goto(x, y)
    t.goto(x, y+100)
    t.goto(x+40, y+100)
    

def d(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x, y+100)
    t.goto(x+40, y+75)
    t.goto(x+40, y)
    t.goto(x, y)



# Extra Shapes

def fill(ax, ay, bx, by, color):
    t.setheading(90)
    t.penup()
    t.goto(ax, ay)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.goto(ax, by)
    t.goto(bx, by)
    t.goto(bx, ay)
    t.goto(ax, ay)
    t.end_fill()

def rect(ax, ay, bx, by, color):
    t.setheading(90)
    t.penup()
    t.goto(ax, ay)
    t.pendown()
    t.color(color)
    t.goto(ax, by)
    t.goto(bx, by)
    t.goto(bx, ay)
    t.goto(ax, ay)

def line(ax, ay, bx, by, width):
    t.width(width)
    t.penup()
    t.goto(ax, ay)
    t.pendown()
    t.goto(bx, by)
    t.width(1)




# Main functions

def draw():
    print("Running...")

    #--------------------------------------#
    
    a(-200, 0)
    b(-150, 0)
    c(-100, 0)
    d(-50, 0)



    #--------------------------------------#

if __name__ == '__main__':
    draw()
    turtle.done()

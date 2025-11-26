import turtle
import time

t = turtle.Turtle()
t.speed(10)
t.hideturtle()


# Letters

def letter_a(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x+20, y+100)
    t.goto(x+40, y)
    t.penup()
    t.goto(x+10, y+50)
    t.pendown()
    t.goto(x+30, y+50)

def letter_b(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x, y+100)
    t.goto(x+40, y+75)
    t.goto(x+5, y+50)
    t.goto(x+40, y+25)
    t.goto(x+40, y)
    t.goto(x, y)

def letter_c(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x+40, y)
    t.goto(x, y)
    t.goto(x, y+100)
    t.goto(x+40, y+100)
    
def letter_d(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x, y+100)
    t.goto(x+40, y+75)
    t.goto(x+40, y)
    t.goto(x, y)

def letter_e(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x+40, y)
    t.goto(x, y)
    t.goto(x, y+35)
    t.goto(x+30, y+35)
    t.goto(x, y+35)
    t.goto(x, y+100)
    t.goto(x+40, y+100)
    
def letter_f(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x, y+75)
    t.goto(x+35, y+75)
    t.goto(x, y+75)
    t.goto(x, y+100)
    t.goto(x+40, y+100)
    
def letter_g(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x, y+100)
    t.goto(x+40, y+100)
    t.goto(x, y+100)
    t.goto(x, y)
    t.goto(x+40, y)
    t.goto(x+40, y+35)
    t.goto(x+20, y+35)
    
def letter_h(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x, y+100)
    t.goto(x, y+50)
    t.goto(x+40, y+50)
    t.goto(x+40, y)
    t.goto(x+40, y+100)
    
def letter_i(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x+40, y)
    t.goto(x+20, y)
    t.goto(x+20, y+100)
    t.goto(x, y+100)
    t.goto(x+40, y+100)
    
def letter_j(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x, y+35)
    t.goto(x, y)
    t.goto(x+40, y)
    t.goto(x+40, y+100)
    t.goto(x, y+100)
    
def letter_k(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x, y+100)
    t.goto(x, y+50)
    t.goto(x+40, y+100)
    t.goto(x, y+50)
    t.goto(x+40, y)

def letter_l(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x, y+100)
    t.goto(x, y)
    t.goto(x+40, y)

def letter_m(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x, y+100)
    t.goto(x+20, y+50)
    t.goto(x+40, y+100)
    t.goto(x+40, y)

def letter_n(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x, y+100)
    t.goto(x+40, y)
    t.goto(x+40, y+100)

def letter_o(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x, y+100)
    t.goto(x+40, y+100)
    t.goto(x+40, y)
    t.goto(x, y)

def letter_p(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x, y+100)
    t.goto(x+40, y+100)
    t.goto(x+40, y+60)
    t.goto(x, y+60)

def letter_q(x, y):
    t.penup()
    t.goto(x+40, y)
    t.pendown()
    t.goto(x+40, y+100)
    t.goto(x, y+100)
    t.goto(x, y+60)
    t.goto(x+40, y+60)

def letter_r(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x, y+100)
    t.goto(x+40, y+100)
    t.goto(x+40, y+50)
    t.goto(x, y+50)
    t.goto(x+40, y)

def letter_s(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x+40, y)
    t.goto(x+40, y+50)
    t.goto(x, y+50)
    t.goto(x, y+100)
    t.goto(x+40, y+100)

def letter_t(x, y):
    t.penup()
    t.goto(x+20, y)
    t.pendown()
    t.goto(x+20, y+100)
    t.goto(x, y+100)
    t.goto(x+40, y+100)

def letter_u(x, y):
    t.penup()
    t.goto(x+20, y)
    t.pendown()
    t.goto(x, y+100)
    t.goto(x, y)
    t.goto(x+40, y)
    t.goto(x+40, y+100)


#------------------------------------------------------------#
    

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
    
    letter_a(-200, 150)
    letter_b(-150, 150)
    letter_c(-100, 150)
    letter_d(-50, 150)
    letter_e(0, 150)
    letter_f(50, 150)
    letter_g(100, 150)
    letter_h(150, 150)
    
    letter_i(-200, 0)
    letter_j(-150, 0)
    letter_k(-100, 0)
    letter_l(-50, 0)
    letter_m(0, 0)
    letter_n(50, 0)
    letter_o(100, 0)
    letter_p(150, 0)

    letter_q(-200, -150)
    letter_r(-150, -150)
    letter_s(-100, -150)
    letter_t(-50, -150)
    letter_u(0, -150)



    #--------------------------------------#

if __name__ == '__main__':
    draw()
    turtle.done()

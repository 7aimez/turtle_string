import turtle

t = turtle.Turtle()


# Extended Logging

log = []

def addToLog(text):
    if text:
        log.append(text)
        print(text)

def printLog():
    print(log)

# Letters and Space
letters = {
    'a': lambda x, y: (t.penup(), t.goto(x, y), t.pendown(), t.goto(x + 20, y + 100), t.goto(x + 40, y), t.penup(), t.goto(x + 10, y + 50), t.pendown(), t.goto(x + 30, y + 50)),
    'b': lambda x, y: (t.penup(), t.goto(x, y), t.pendown(), t.goto(x, y + 100), t.goto(x + 40, y + 75), t.goto(x + 5, y + 50), t.goto(x + 40, y + 25), t.goto(x + 40, y), t.goto(x, y)),
    'c': lambda x, y: (t.penup(), t.goto(x, y), t.pendown(), t.goto(x + 40, y), t.goto(x, y), t.goto(x, y + 100), t.goto(x + 40, y + 100)),
    'd': lambda x, y: (t.penup(), t.goto(x, y), t.pendown(), t.goto(x, y + 100), t.goto(x + 40, y + 75), t.goto(x + 40, y), t.goto(x, y)),
    'e': lambda x, y: (t.penup(), t.goto(x, y), t.pendown(), t.goto(x + 40, y), t.goto(x, y), t.goto(x, y + 35), t.goto(x + 30, y + 35), t.goto(x, y + 35), t.goto(x, y + 100), t.goto(x + 40, y + 100)),
    'f': lambda x, y: (t.penup(), t.goto(x, y), t.pendown(), t.goto(x, y + 75), t.goto(x + 35, y + 75), t.goto(x, y + 75), t.goto(x, y + 100), t.goto(x + 40, y + 100)),
    'g': lambda x, y: (t.penup(), t.goto(x, y), t.pendown(), t.goto(x, y + 100), t.goto(x + 40, y + 100), t.goto(x, y + 100), t.goto(x, y), t.goto(x + 40, y), t.goto(x + 40, y + 35), t.goto(x + 20, y + 35)),
    'h': lambda x, y: (t.penup(), t.goto(x, y), t.pendown(), t.goto(x, y + 100), t.goto(x, y + 50), t.goto(x + 40, y + 50), t.goto(x + 40, y), t.goto(x + 40, y + 100)),
    'i': lambda x, y: (t.penup(), t.goto(x, y), t.pendown(), t.goto(x + 40, y), t.goto(x + 20, y), t.goto(x + 20, y + 100), t.goto(x, y + 100), t.goto(x + 40, y + 100)),
    'j': lambda x, y: (t.penup(), t.goto(x, y), t.pendown(), t.goto(x, y + 35), t.goto(x, y), t.goto(x + 40, y), t.goto(x + 40, y + 100), t.goto(x, y + 100)),
    'k': lambda x, y: (t.penup(), t.goto(x, y), t.pendown(), t.goto(x, y + 100), t.goto(x, y + 50), t.goto(x + 40, y + 100), t.goto(x, y + 50), t.goto(x + 40, y)),
    'l': lambda x, y: (t.penup(), t.goto(x, y), t.pendown(), t.goto(x, y + 100), t.goto(x, y), t.goto(x + 40, y)),
    'm': lambda x, y: (t.penup(), t.goto(x, y), t.pendown(), t.goto(x, y + 100), t.goto(x + 20, y + 50), t.goto(x + 40, y + 100), t.goto(x + 40, y)),
    'n': lambda x, y: (t.penup(), t.goto(x, y), t.pendown(), t.goto(x, y + 100), t.goto(x + 40, y), t.goto(x + 40, y + 100)),
    'o': lambda x, y: (t.penup(), t.goto(x, y), t.pendown(), t.goto(x, y + 100), t.goto(x + 40, y + 100), t.goto(x + 40, y), t.goto(x, y)),
    'p': lambda x, y: (t.penup(), t.goto(x, y), t.pendown(), t.goto(x, y + 100), t.goto(x + 40, y + 100), t.goto(x + 40, y + 60), t.goto(x, y + 60)),
    'q': lambda x, y: (t.penup(), t.goto(x + 40, y), t.pendown(), t.goto(x + 40, y + 100), t.goto(x, y + 100), t.goto(x, y + 60), t.goto(x + 40, y + 60)),
    'r': lambda x, y: (t.penup(), t.goto(x, y), t.pendown(), t.goto(x, y + 100), t.goto(x + 40, y + 100), t.goto(x + 40, y + 50), t.goto(x, y + 50), t.goto(x + 40, y)),
    's': lambda x, y: (t.penup(), t.goto(x, y), t.pendown(), t.goto(x + 40, y), t.goto(x + 40, y + 50), t.goto(x, y + 50), t.goto(x, y + 100), t.goto(x + 40, y + 100)),
    't': lambda x, y: (t.penup(), t.goto(x + 20, y), t.pendown(), t.goto(x + 20, y + 100), t.goto(x, y + 100), t.goto(x + 40, y + 100)),
    'u': lambda x, y: (t.penup(), t.goto(x, y), t.pendown(), t.goto(x, y + 100), t.goto(x, y), t.goto(x + 40, y), t.goto(x + 40, y + 100)),
    'v': lambda x, y: (t.penup(), t.goto(x, y + 100), t.pendown(), t.goto(x + 20, y), t.goto(x + 40, y + 100)),
    'w': lambda x, y: (t.penup(), t.goto(x, y + 100), t.pendown(), t.goto(x + 10, y), t.goto(x + 20, y + 50), t.goto(x + 30, y), t.goto(x + 40, y + 100)),
    'x': lambda x, y: (t.penup(), t.goto(x, y + 100), t.pendown(), t.goto(x + 40, y), t.goto(x + 20, y + 50), t.goto(x, y), t.goto(x + 40, y + 100)),
    'y': lambda x, y: (t.penup(), t.goto(x + 20, y), t.pendown(), t.goto(x + 20, y + 50), t.goto(x, y + 100), t.goto(x + 20, y + 50), t.goto(x + 40, y + 100)),
    'z': lambda x, y: (t.penup(), t.goto(x, y + 100), t.pendown(), t.goto(x + 40, y + 100), t.goto(x, y), t.goto(x + 40, y)),
    ' ': lambda x, y: (x + 50),
}

# Special Characters    
special_characters = {
    '1': lambda x, y: (t.penup(), t.goto(x, y), t.pendown(), t.goto(x, y + 5), t.goto(x + 5, y + 5), t.goto(x + 5, y), t.goto(x, y)),
    '2': lambda x, y: (t.penup(), t.goto(x, y), t.pendown(), t.goto(x, y + 5), t.goto(x + 5, y + 5), t.goto(x + 5, y), t.goto(x, y), t.penup(), t.goto(x, y + 30), t.pendown(), t.goto(x, y + 100), t.goto(x + 5, y + 100), t.goto(x + 5, y + 30), t.goto(x, y + 30)),
    '3': lambda x, y: (t.penup(), t.goto(x + 5, y), t.pendown(), t.goto(x + 5, y + 5), t.goto(x + 10, y + 5), t.goto(x + 10, y - 10), t.goto(x, y - 10), t.goto(x, y - 5), t.goto(x + 5, y - 5), t.goto(x + 5, y)),
    '4': lambda x, y: (t.penup(), t.goto(x + 17.5, y + 100), t.pendown(), t.goto(x + 22.5, y + 100), t.goto(x + 22.5, y + 90), t.goto(x + 17.5, y + 90), t.goto(x + 17.5, y + 100)),
    '5': lambda x, y: (t.penup(), t.goto(x, y), t.pendown(), t.goto(x, y + 5), t.goto(x + 5, y + 5), t.goto(x + 5, y), t.goto(x, y), t.penup(), t.goto(x, y + 30), t.pendown(), t.goto(x, y + 50), t.goto(x + 35, y + 50), t.goto(x + 35, y + 95), t.goto(x, y + 95), t.goto(x, y + 100), t.goto(x + 40, y + 100), t.goto(x + 40, y + 45), t.goto(x + 5, y + 45), t.goto(x + 5, y + 30), t.goto(x, y + 30)),
}

def draw_text(text, pensize, start_x, start_y, spacing, line_height, speed):
    t.speed(0)
    t.pensize(pensize)
    # Special Characters
    sc_text = text.replace(".", "1").replace("!", "2").replace(",", "3").replace("'", "4").replace("?", "5").replace("/", "\n")
    x = start_x # Set the first x to the start_x
    y = start_y # Set the first y to the start_y
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()
    t.speed(speed)
    for letter in sc_text.lower():
        if letter == '\n':
            y -= line_height
            x = start_x
        elif letter in letters:
            func = letters[letter]
            if letter == ' ':
                x += spacing # Add spacing with no letter
            else:
                func(x, y)
                x += spacing # Add spacing after letter
        elif letter in special_characters:
            special_characters[letter](x, y)
            x += spacing # Add spacing after special character

def draw_bg():
    t.penup()
    t.goto(-1000, 1000)
    t.pendown()
    t.begin_fill()
    t.goto(1000, 1000)
    t.goto(1000, -1000)
    t.goto(-1000, -1000)
    t.goto(-1000, 1000)
    t.end_fill()

def main():
    setup = {
        "text": "This is/sample/text!",
        "speed": 5,
        "pensize": 10,
        "start_x": -200,
        "start_y": 100,
        "spacing": 60,
        "line_height": 150,
        "show_turtle": True,
        "turtle_shape": "circle",
        "color": "darkblue",
        "bg": "#ebebeb",
    }
    addToLog("\n\nRunning...")
    t.shape(setup["turtle_shape"])
    if setup["show_turtle"]:
        t.showturtle()
    else:
        t.hideturtle()
    t.speed(0)
    t.color(setup["bg"])
    draw_bg()
    t.speed(setup["speed"])
    t.color(setup["color"])
    draw_text(setup["text"], setup["pensize"], setup["start_x"], setup["start_y"], setup["spacing"], setup["line_height"], setup["speed"])

if __name__ == '__main__':
    main()
    t.hideturtle()
    turtle.done()

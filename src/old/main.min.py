import turtle
t=turtle.Turtle()
t.speed(10)
t.hideturtle()
log=[]
def addToLog(text):
	if text:log.append(text);print(text)
def printLog():print(log)
def letter_a(x,y):t.penup();t.goto(x,y);t.pendown();t.goto(x+20,y+100);t.goto(x+40,y);t.penup();t.goto(x+10,y+50);t.pendown();t.goto(x+30,y+50)
def letter_b(x,y):t.penup();t.goto(x,y);t.pendown();t.goto(x,y+100);t.goto(x+40,y+75);t.goto(x+5,y+50);t.goto(x+40,y+25);t.goto(x+40,y);t.goto(x,y)
def letter_c(x,y):t.penup();t.goto(x,y);t.pendown();t.goto(x+40,y);t.goto(x,y);t.goto(x,y+100);t.goto(x+40,y+100)
def letter_d(x,y):t.penup();t.goto(x,y);t.pendown();t.goto(x,y+100);t.goto(x+40,y+75);t.goto(x+40,y);t.goto(x,y)
def letter_e(x,y):t.penup();t.goto(x,y);t.pendown();t.goto(x+40,y);t.goto(x,y);t.goto(x,y+35);t.goto(x+30,y+35);t.goto(x,y+35);t.goto(x,y+100);t.goto(x+40,y+100)
def letter_f(x,y):t.penup();t.goto(x,y);t.pendown();t.goto(x,y+75);t.goto(x+35,y+75);t.goto(x,y+75);t.goto(x,y+100);t.goto(x+40,y+100)
def letter_g(x,y):t.penup();t.goto(x,y);t.pendown();t.goto(x,y+100);t.goto(x+40,y+100);t.goto(x,y+100);t.goto(x,y);t.goto(x+40,y);t.goto(x+40,y+35);t.goto(x+20,y+35)
def letter_h(x,y):t.penup();t.goto(x,y);t.pendown();t.goto(x,y+100);t.goto(x,y+50);t.goto(x+40,y+50);t.goto(x+40,y);t.goto(x+40,y+100)
def letter_i(x,y):t.penup();t.goto(x,y);t.pendown();t.goto(x+40,y);t.goto(x+20,y);t.goto(x+20,y+100);t.goto(x,y+100);t.goto(x+40,y+100)
def letter_j(x,y):t.penup();t.goto(x,y);t.pendown();t.goto(x,y+35);t.goto(x,y);t.goto(x+40,y);t.goto(x+40,y+100);t.goto(x,y+100)
def letter_k(x,y):t.penup();t.goto(x,y);t.pendown();t.goto(x,y+100);t.goto(x,y+50);t.goto(x+40,y+100);t.goto(x,y+50);t.goto(x+40,y)
def letter_l(x,y):t.penup();t.goto(x,y);t.pendown();t.goto(x,y+100);t.goto(x,y);t.goto(x+40,y)
def letter_m(x,y):t.penup();t.goto(x,y);t.pendown();t.goto(x,y+100);t.goto(x+20,y+50);t.goto(x+40,y+100);t.goto(x+40,y)
def letter_n(x,y):t.penup();t.goto(x,y);t.pendown();t.goto(x,y+100);t.goto(x+40,y);t.goto(x+40,y+100)
def letter_o(x,y):t.penup();t.goto(x,y);t.pendown();t.goto(x,y+100);t.goto(x+40,y+100);t.goto(x+40,y);t.goto(x,y)
def letter_p(x,y):t.penup();t.goto(x,y);t.pendown();t.goto(x,y+100);t.goto(x+40,y+100);t.goto(x+40,y+60);t.goto(x,y+60)
def letter_q(x,y):t.penup();t.goto(x+40,y);t.pendown();t.goto(x+40,y+100);t.goto(x,y+100);t.goto(x,y+60);t.goto(x+40,y+60)
def letter_r(x,y):t.penup();t.goto(x,y);t.pendown();t.goto(x,y+100);t.goto(x+40,y+100);t.goto(x+40,y+50);t.goto(x,y+50);t.goto(x+40,y)
def letter_s(x,y):t.penup();t.goto(x,y);t.pendown();t.goto(x+40,y);t.goto(x+40,y+50);t.goto(x,y+50);t.goto(x,y+100);t.goto(x+40,y+100)
def letter_t(x,y):t.penup();t.goto(x+20,y);t.pendown();t.goto(x+20,y+100);t.goto(x,y+100);t.goto(x+40,y+100)
def letter_u(x,y):t.penup();t.goto(x,y);t.pendown();t.goto(x,y+100);t.goto(x,y);t.goto(x+40,y);t.goto(x+40,y+100)
def letter_v(x,y):t.penup();t.goto(x,y+100);t.pendown();t.goto(x+20,y);t.goto(x+40,y+100)
def letter_w(x,y):t.penup();t.goto(x,y+100);t.pendown();t.goto(x+10,y);t.goto(x+20,y+50);t.goto(x+30,y);t.goto(x+40,y+100)
def letter_x(x,y):t.penup();t.goto(x,y+100);t.pendown();t.goto(x+40,y);t.goto(x+20,y+50);t.goto(x,y);t.goto(x+40,y+100)
def letter_y(x,y):t.penup();t.goto(x+20,y);t.pendown();t.goto(x+20,y+50);t.goto(x,y+100);t.goto(x+20,y+50);t.goto(x+40,y+100)
def letter_z(x,y):t.penup();t.goto(x,y+100);t.pendown();t.goto(x+40,y+100);t.goto(x,y);t.goto(x+40,y)
def letter_1(x,y):t.penup();t.goto(x,y);t.pendown();t.goto(x,y+5);t.goto(x+5,y+5);t.goto(x+5,y);t.goto(x,y)
def letter_2(x,y):t.penup();t.goto(x,y);t.pendown();t.goto(x,y+5);t.goto(x+5,y+5);t.goto(x+5,y);t.goto(x,y);t.penup();t.goto(x,y+10);t.pendown();t.goto(x,y+100);t.goto(x+5,y+100);t.goto(x+5,y+10);t.goto(x,y+10)
def letter_3(x,y):t.penup();t.goto(x+5,y);t.pendown();t.goto(x+5,y+5);t.goto(x+10,y+5);t.goto(x+10,y-10);t.goto(x,y-10);t.goto(x,y-5);t.goto(x+5,y-5);t.goto(x+5,y)
def draw_text(text,start_x,start_y,spacing=50,line_height=150):
	sc_text=text.replace('.','1').replace('!','2').replace(',','3');x=start_x;y=start_y
	for letter in sc_text.lower():
		if letter=='\n':y-=line_height;x=start_x
		else:
			func_name='letter_'+letter;letter_func=globals().get(func_name)
			if letter_func:letter_func(x,y)
			x+=spacing
def main():addToLog('Running...');text='This,\nis a...\nsample!';draw_text(text,-200,100,spacing=50)
if __name__=='__main__':main();turtle.done()

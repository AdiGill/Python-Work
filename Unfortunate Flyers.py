from tkinter import *
from time import *
from random import *
from math import *
tk = Tk()
s = Canvas(tk, width=1000, height=1000, background="#0B071E")
s.pack()


x = randint(0,1000)
y = randint(0,1000)
sz = randint(0,5)
for n in range(175):
    x = randint(0,1000)
    y = randint(0,1000)
    sz = randint(1,5)
    s.create_oval(x,y,x+sz,y+sz, fill = "white")

s.create_oval(650,650,1000,1000,fill = "blue")
s.create_polygon(700,700,800,650,950,700,1000,850,850,1000, fill = "green", smooth = True)
s.create_polygon(650,800,750,850,800,950,700,950, fill = "green", smooth = True)
s.create_polygon(0,0,200,0,175,50,200,100,100,200,50,150,0,200,fill = "white")
s.create_polygon(200,0,175,50,0,0,fill = "sky blue",outline = "white", width = 5)

x1 = 0
x2 = x1-50
x3 = x1-25
x4 = x1+25
x5 = x1+50
x6 = x1+75
x7 = x1+125
x8 = x1+100
x9 = x1+150

y1 = 500
y2 = y1+50
y3 = y1+150
y4 = y1+200
y5 = y1-20
y6 = y1-100



sx1 = 550
sx2 = sx1 - 50
sy1 = 50
sy2 = sy1 + 50
for f in range(100):
    cord = s.create_line(150,150,250,250,x1,y1+50, fill = "grey",width = 5, smooth = True)
    astronaut = s.create_polygon(x1,y1,x2,y1,x2,y2,x1,y2,x1,y3,x3,y4,x4,y4,x5,y3,x6,y4,x7,y4,x8,y3,x8,y2,x9,y2,x9,y1,x6,y1,x6,y5,x4,y5,x4,y1,fill = "white")
    head = s.create_oval(x1,y6,x8,y1, fill = "sky blue", outline = "white", width = 8)
    scrap = s.create_polygon(sx1,sy1,sx1,sy2,sx2,sy2,fill = "black")
    s.update()
    sleep(0.03)
    s.delete(astronaut,head,cord,scrap)
    
    x1 = x1+5
    x2 = x1-50
    x3 = x1-25
    x4 = x1+25
    x5 = x1+50
    x6 = x1+75
    x7 = x1+125
    x8 = x1+100
    x9 = x1+150

    y1 = y1
    y2 = y1+50
    y3 = y1+150
    y4 = y1+200
    y5 = y1-20
    y6 = y1-100
    sx1 = sx1 - 2.15
    sy1 = sy1 + 2.15
    
    sx2 = sx1 - 50
    
    sy2 = sy1 + 50

#x = xCentre + r*cos(b*f)
#y = yCentre – r*sin(b*f)
xc = x1
yc = y6
r = 300

#INTERCEPT POINT: 250,350
for f in range(100):
    scrap = s.create_polygon(sx1,sy1,sx1,sy2,sx2,sy2,fill = "black")
    cord = s.create_line(150,150,250,250,150,350, fill = "grey",width = 5, smooth = True)
    cord2 = s.create_line(randint(250,275),randint(350,375),randint(450,475),randint(550,575),x1,y1+50, fill = "grey",width = 5, smooth = True)
    astronaut = s.create_polygon(x1,y1,x2,y1,x2,y2,x1,y2,x1,y3,x3,y4,x4,y4,x5,y3,x6,y4,x7,y4,x8,y3,x8,y2,x9,y2,x9,y1,x6,y1,x6,y5,x4,y5,x4,y1,fill = "white")
    head = s.create_oval(x1,y6,x8,y1, fill = "sky blue", outline = "white", width = 8)
    
    s.update()
    sleep(0.03)
    s.delete(astronaut,head,cord,cord2,scrap)

    x1 = xc + r*cos(.2*f)
    x2 = x1-50
    x3 = x1-25
    x4 = x1+25
    x5 = x1+50
    x6 = x1+75
    x7 = x1+125
    x8 = x1+100
    x9 = x1+150
    xc = xc + 10

    y1 = yc - r*sin(.2*f)
    y2 = y1+50
    y3 = y1+150
    y4 = y1+200
    y5 = y1-20
    y6 = y1-100

    sx1 = sx1 - 2
    sy1 = sy1 + 2
    
    sx2 = sx1 - 50
    
    sy2 = sy1 + 50







spacing = 50



for x in range(0, 1000, spacing):
    s.create_line( x, 25, x, 1000, fill="white")
    s.create_text( x, 5, text=str(x), font="Times 9", anchor = N,fill = "white")

for y in range(0, 1000, spacing):
    s.create_line( 25, y, 1000, y, fill="white")
    s.create_text( 5, y, text=str(y), font="Times 9", anchor = W,fill = "white")

s.update()

 
 

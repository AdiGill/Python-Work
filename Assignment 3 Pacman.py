from tkinter import *
from time import *
from random import *
tk = Tk()
screen = Canvas(tk, width=1000, height=1000, background="black")
screen.pack()



x1 = 0
y1 = 150
x2 = 300
y2 = 350
mid = x1-x2
m=310.9
s = 25
ms = 3
#s = 0 when m is 359
#s = 25 when m is 310

#ghost:

x3 = 1270
x4 = x3 + 50
x5 = x4+50
x6 = x5+50
x7 = x6+50
x8 = x7+50
x9=x3+50
y3 = 100
y4 = y3+250
y5 = y4-50
y6=y3+50
for f in range(300):
    x1 = x1 + 4
    x2 = x1 +200
    if 310< m <= 359.9:
        m = m + ms
        s=s-ms/2
    else:
        ms = ms * -1
        m = m + ms
        
    
    
    
    pacman = screen.create_arc(x1,y1,x2,y2,fill= "yellow", start = s, extent = m)
    screen.update()
    sleep(0.01)
    screen.delete(pacman)

s = 190
for f in range(500):
    x1 = x1 - 4
    x2 = x1 - 200
    if 310< m <= 359.9:
        m = m + ms
        s=s-ms/2
    else:
        ms = ms * -1
        m = m + ms
            
    x9=x3+50
    x10=x9+100
    x3 = x3 - 4
    x4 = x3 + 50
    x5 = x4+50
    x6 = x5+50
    x7 = x6+50
    x8 = x7+50
    
    
    y3 = 100
    y4 = y3+250
    y5 = y4-50
    y6=y3+50
    y7=y6
    
    ghost = screen.create_polygon(x3,y3,x3,y4,x4,y4,x4,y5,x5,y5,x5,y4,x6,y4,x6,y5,x7,y5,x7,y4,x8,y4,x8,y3,fill="blue")
    eye1 = screen.create_rectangle(x9,y6,x9+50,y6+50,fill="black",outline="white",width = 10)
    eye2 = screen.create_rectangle(x10,y7,x10+50,y7+50,fill="black",outline="white",width = 10)
    pacman = screen.create_arc(x2,y1,x1,y2,fill= "yellow", start = s, extent = m)
    screen.update()
    sleep(0.01)
    screen.delete(pacman,ghost,eye1,eye2)






spacing = 50

for x in range(0, 1000, spacing): 
    screen.create_line( x, 25, x, 1000, fill="white")
    screen.create_text( x, 5, text=str(x), font="Times 9", anchor = N)

for y in range(0, 1000, spacing):
    screen.create_line( 25, y, 1000, y, fill="white")
    screen.create_text( 5, y, text=str(y), font="Times 9", anchor = W,fill = "white")

screen.update()


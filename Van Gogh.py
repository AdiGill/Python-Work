from tkinter import *
from time import *
from random import *
tk = Tk()
screen = Canvas(tk, width=1000, height=1000, background="black")
screen.pack()
x=1
x1=0
y1=100
x2=100
y2=200
for hz in range(8):
    
    for sq in range(8):
        
        if x2 < 900:
            x1 = x1 + 100
            x2 = x2 + 100
            
        else :
            x1 = 100
            x2 = 200
            y1 = y1 + 100
            y2 = y2 + 100
            if x == 1:
                color = "orange"
                x = x + 1
            else:
                color = "purple"
                x = x - 1
            
        if x == 1:
            color = "orange"
            x = x + 1
        else:
            color = "purple"
            x = x - 1
            
            
        
            
        
        
        for dot in range(75):
            
            
            dx1 = randint(x1,x2)
            dy1 = randint(y1,y2)
            s = randint(1,5)
            dx2 = dx1 + s
            dy2 = dy1 + s
            screen.create_rectangle(dx1,dy1,dx2,dy2,fill = color, outline = color)
    
    
        
    


##
##spacing = 50
##
##for x in range(0, 1000, spacing): 
##    screen.create_line( x, 25, x, 1000, fill="white")
##    screen.create_text( x, 5, text=str(x), font="Times 9", anchor = N)
##
##for y in range(0, 1000, spacing):
##    screen.create_line( 25, y, 1000, y, fill="white")
##    screen.create_text( 5, y, text=str(y), font="Times 9", anchor = W,fill = "white")
##
##screen.update()
##

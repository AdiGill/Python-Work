
from tkinter import *
from time import *
from random import *
from math import *
tk = Tk()
s = Canvas(tk, width=1000, height=1000, background="#F7D6BD")
s.pack()
 
l = 0
s.create_polygon(300,100,875,525,950,450,900,450,fill = "grey", outline = "black", width = 1.5)
s.create_polygon(1300,450,500,200,-300,225,0,-200,1000,-200,fill = "#14192e", smooth = True)
s.create_polygon(400,175,415,0,1000,0,1000,300,fill = "grey")

#Single Right Hair Strand DO NOT DELETE(again)
s.create_polygon(950,0,850,300,800,0, fill = "#b5b5b5",outline = "black", width = 2)
#SCAR
s.create_polygon(575,300,585,325,525,1000,575,1000,605,325,625,300,fill = "#877161",outline = "#1C1713", width = 3)

#Mask
s.create_polygon(1000,800,600,900,0,950,0,1000,1000,1000,fill = "#14192e")
#eye brow = s.create_polygon(750,435,875,525,875,650,850,625,850,575,fill = "#877161")#


#shadow = s.create_polygon(750,435,875,525,875,650,850,625,850,575,fill = "#877161")
s.create_polygon(750,435,875,525,875,650,850,625,850,575,fill = "#877161")
#lines = #
s.create_line(960,450,950,500,900,550,fill = "black",width = 3)

for blink in range(10):
    eye2 = s.create_polygon(900,700,300,700,50,250,700,350,fill = "white",outline = "black",width = 15,smooth = True)
    eye3 = s.create_polygon(900,750,300,700,150,350,700,350,fill = "white",smooth = True)
    
    pupil = s.create_oval(400,400,700,700,fill="black",outline="black")
    s.create_oval(900,50,1100,250,fill = "grey",outline = "#333333",width = 5)
    s.create_polygon(750,435,875,525,875,650,850,625,850,575,fill = "#877161")
    #Line Detail
    s.create_line(960,450,950,500,900,550,fill = "black",width = 3)
    s.create_line(900,750,850,750,750,850,fill = "black",width = 3)
    s.create_line(825,725,775,765,fill = "black",width = 3)
    s.create_line(835,725,775,775,fill = "black",width = 3)

    
    s.create_polygon(300,100,875,525,950,450,900,450,fill = "grey", outline = "black", width = 1.5)
    
    s.create_polygon(1300,450,500,200,-300,225,0,-200,1000,-200,fill = "#14192e", smooth = True)
    s.create_polygon(400,175,415,0,1000,0,1000,300,fill = "grey")
    s.create_oval(900,50,1100,250,fill = "grey",outline = "#333333",width = 5)
    s.create_oval(950,100,1050,200,fill = "grey",outline = "#333333",width = 5)
    s.create_polygon(950,0,850,300,800,0, fill = "#b5b5b5",outline = "black", width = 2)
    s.create_polygon(850,300,875,225,840,0,800,0,fill = "#a1a1a1")
    s.create_polygon(350,0,200,550,150,0,fill = "#b5b5b5",outline = "black", width = 2)
    s.create_polygon(227,450,200,0,150,0,200,550,fill = "#a1a1a1")
    s.create_polygon(0,0,100,600,200,0,fill = "#b5b5b5",outline = "black", width = 2)
    s.create_polygon(100,600,110,550,20,0,0,0,fill = "#a1a1a1")
    
    
    
    l = l + 1
    if l >= 5:
        cover = s.create_polygon(100,275,350,275,650,325,825,475,900,650,800,800,100,800, fill = "#F7D6BD")
        s.create_polygon(575,300,585,325,525,1000,575,1000,605,325,625,300,fill = "#877161",outline = "#1C1713", width = 3)
        
        #Mask
        s.create_polygon(1000,800,600,900,0,950,0,1000,1000,1000,fill = "#14192e")
        
        s.create_polygon(750,435,875,525,875,650,850,625,850,575,fill = "#877161")
        s.create_line(960,450,950,500,900,550,fill = "black",width = 3)
        s.create_line(900,750,850,750,750,850,fill = "black",width = 3)
        s.create_line(825,725,775,765,fill = "black",width = 3)
        s.create_line(835,725,775,775,fill = "black",width = 3)
        s.create_polygon(300,100,875,525,950,450,900,450,fill = "grey", outline = "black", width = 1.5)
        s.create_polygon(1300,450,500,200,-300,225,0,-200,1000,-200,fill = "#14192e", smooth = True)
        s.create_polygon(400,175,415,0,1000,0,1000,300,fill = "grey")
        b = s.create_line(150,350,450,600,825,600,fill = "black",width = 6, smooth = True)
        s.create_oval(900,50,1100,250,fill = "grey",outline = "#333333",width = 5)
        s.create_oval(950,100,1050,200,fill = "grey",outline = "#333333",width = 5)
        s.create_polygon(950,0,850,300,800,0, fill = "#b5b5b5",outline = "black", width = 2)
        s.create_polygon(950,0,850,300,800,0, fill = "#b5b5b5",outline = "black", width = 2)
        s.create_polygon(850,300,875,225,840,0,800,0,fill = "#a1a1a1")
        s.create_polygon(350,0,200,550,150,0,fill = "#b5b5b5",outline = "black", width = 2)
        s.create_polygon(227,450,200,0,150,0,200,550,fill = "#a1a1a1")
        s.create_polygon(0,0,100,600,200,0,fill = "#b5b5b5",outline = "black", width = 2)
        s.create_polygon(100,600,110,550,20,0,0,0,fill = "#a1a1a1")
        s.update()
        
    s.update()
    sleep(0.3)
    s.delete(eye2,eye3,pupil)
    
s.delete(b,cover)
 
s.create_polygon(750,435,875,525,875,650,850,625,850,575,fill = "#877161")
s.create_line(960,450,950,500,900,550,fill = "black",width = 3)
s.create_line(900,750,850,750,750,850,fill = "black",width = 3)
s.create_line(825,725,775,765,fill = "black",width = 3)
s.create_line(835,725,775,775,fill = "black",width = 3)
s.create_polygon(900,700,300,700,50,250,700,350,fill = "white",outline = "black",width = 15,smooth = True)
s.create_polygon(900,750,300,700,150,350,700,350,fill = "white",smooth = True)
 
s.create_oval(400,400,700,700,fill="red",outline="black",width = 10)
s.create_oval(475,475,625,625,fill="red",outline = "black",width = 2)
s.create_oval(525,525,575,575,fill="black")
 
 
s.create_oval(650,550,690,590,fill = "white",outline="white")
 
 

 
s.create_polygon(950,0,850,300,800,0, fill = "#b5b5b5",outline = "black", width = 2)
s.create_polygon(850,300,875,225,840,0,800,0,fill = "#a1a1a1")
s.create_polygon(350,0,200,550,150,0,fill = "#b5b5b5",outline = "black", width = 2)
s.create_polygon(227,450,200,0,150,0,200,550,fill = "#a1a1a1")
s.create_polygon(0,0,100,600,200,0,fill = "#b5b5b5",outline = "black", width = 2)
s.create_polygon(100,600,110,550,20,0,0,0,fill = "#a1a1a1")
yd = 820
s.create_polygon(300,640,550,710,800,695,750,800,700,750,650,yd,600,yd,500,yd-100,fill = "#ab0a02",smooth = True)
xCentre = 540
yCentre = 542
a = 3
f = .2
 
for o in range(250):
    x = xCentre + a*cos(f*o)
    y = yCentre - a*sin(f*o)
    cxCentre = x + 12.5
    cyCentre = y + 12.5
    
    
    
    sharingan = s.create_oval(x,y,x+25,y+25,fill="black",outline = "black", width = 2)
    sharingan4 = s.create_polygon(x,y,x+30,y+20,x+36,y+15,fill="black",outline = "black", width = 3, smooth = True)
    x = xCentre + a*cos(f*o-2)
    y = yCentre - a*sin(f*o-2)
    sharingan2 = s.create_oval(x,y,x+25,y+25,fill="black",outline = "black", width = 2)
    sharingan5 = s.create_polygon(x,y,x+30,y+20,x+36,y+15,fill="black",outline = "black", width = 3, smooth = True)
    x = xCentre + a*cos(f*o-4)
    y = yCentre - a*sin(f*o-4)
    sharingan3 = s.create_oval(x,y,x+25,y+25,fill="black",outline = "black", width = 2)
    sharingan6 = s.create_polygon(x,y,x+30,y+20,x+36,y+15,fill="black",outline = "black", width = 3, smooth = True)
    yd = yd + 1
    blood = s.create_polygon(285,625,550,710,800,695,750,800,700,750,650,yd,600,yd,500,yd-100,fill = "#ab0a02",smooth = True)
    mask = s.create_polygon(1000,800,600,900,0,950,0,1000,1000,1000,fill = "#14192e")
    s.update()
    sleep(0.03)
    s.delete(sharingan,sharingan2,sharingan3,sharingan4,sharingan5,sharingan6,blood,mask)
    if a<75:
        a=a+.8
    else:
        f = f +.00002
 
 
spacing = 50
 
for x in range(0, 1000, spacing):
    s.create_line( x, 25, x, 1000, fill="white")
    s.create_text( x, 5, text=str(x), font="Times 9", anchor = N)
 
for y in range(0, 1000, spacing):
    s.create_line( 25, y, 1000, y, fill="white")
    s.create_text( 5, y, text=str(y), font="Times 9", anchor = W,fill = "white")
 
s.update()
 

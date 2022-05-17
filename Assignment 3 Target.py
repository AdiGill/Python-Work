from math import *
from tkinter import *
from time import *
from random import *
tk = Tk()
screen = Canvas(tk, width=800, height=800, background="black")
screen.pack()

rx = 0
ry = 0
d = 800
rx2=800
ry2 = 800
r=d/2

for rings in range (6):
      screen.create_oval(rx,ry,rx2,ry2,fill="black",outline="white",width=2)
      d=d-75
      rx=rx+75
      ry=ry+75
      rx2=rx2-75
      ry2=ry2-75

      
        

        


diameter = 25
radius = diameter/2
x1 = 100
y1 = 400
x2 = x1 + diameter
y2 = y1 + diameter
color="red"
xSpeed = 11
ySpeed = -2
xd = x2-400
yd = y2-400


for f in range(1800):
      xd = x2-400+radius
      yd = y2-400+radius

      dist = sqrt((xd**2) + (yd**2))
      print(dist)
      
      ball = screen.create_oval(  x1,  y1,  x2,  y2,  fill=color,outline = color)
      #Update, sleep, delete
      screen.update()
      sleep(0.03)
      screen.delete( ball )

      #Update positions before the next frame
      x1 = x1 + xSpeed  
      y1 = y1 + ySpeed

      x2 = x1 + diameter
      y2 = y1 + diameter
 
      if x2 >= 800:
            xSpeed = -1.0 * xSpeed
        
      if x1<= 0:
            xSpeed = -1 * xSpeed
        
      if y2 >= 800:
            ySpeed = -1.0 * ySpeed
        
      if y1<= 0:
            ySpeed = -1 * ySpeed

     

      if  dist <75 :
            color = "blue"
      elif dist<150 and -87.5<yd<87.5:
            color = "red"
      elif dist<225 and -125<yd<125:
            color = "green"
      elif dist<300 and -162.5<yd<162.5:
            color = "yellow"
      elif dist<475:
            color = "pink"
      elif dist<550:
            color = "grey"
      else:
          color = "grey"



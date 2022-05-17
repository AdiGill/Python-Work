
from tkinter import *
from random import *





master = Tk()
s = Canvas( master, width=1300, height=950, background = "white" )
s.pack()

##Sky:
y=0
y2=y + 200
color = ("#00FBB3","#00FBC6","#00FBD9","#00E8FB","#00B7FB","#007EFB")
for sky in range(6):
    s.create_rectangle(0,y,1300,y2, fill =  color[sky], outline = color[sky],)
    y=y+85
    y2=y+85

###ground
##s.create_rectangle(0,y,1300,y2, fill = "#B8B4A3", outline = "#B8B4A3")
##y=y+50
##y2=y2+100
##s.create_rectangle(0,y,1300,y2, fill = "#C6C2B0", outline = "#C6C2B0")
##y=y+50
##y2=y2+100
##s.create_rectangle(0,y,1300,y2, fill = "#D3CFBC", outline = "#D3CFBC")
##y=y+50
##y2=y2+100
##s.create_rectangle(0,y,1300,y2, fill = "#DDD9C5", outline = "#DDD9C5")
##y=y+50
##y2=y2+100
##s.create_rectangle(0,y,1300,y2, fill = "#E7E3CC", outline = "#E7E3CC")
##y=y+50
##y2=y2+100
##s.create_rectangle(0,y,1300,y2, fill = "#F3EDCE", outline = "#F3EDCE")
##y=y+50
##y2=y2+100
##s.create_rectangle(0,y,1300,y2, fill = "#F3F1E3", outline = "#F3F1E3")
##y=y+50
##y2=y2+100
c=["#B8B4A3","#C6C2B0","#D3CFBC","#DDD9C5","#E7E3CC","#F3EDCE","#F3F1E3"]
for i in range(0,4):
    currFill = c[i]
    s.create_rectangle(0,y,1300,y2, fill = currFill, outline = currFill)
    y = y + 85
    y2 = y + 85

#Patrick
s.create_arc(100,750,300,550, start = 0, extent = 180, fill = "#804707", outline = "black", width = 2)
s.create_line(200,550,200,525,150,525,165,510,150,525,165,540,150,525,250,525, fill = "yellow", width = 3)
s.create_line(240,510,250,545, fill = "yellow", width = 3)
s.create_line(220,510,230,545, fill = "yellow", width = 3)
s.create_polygon(160,555,165,625,115,625, fill = "#A58765", smooth = True)

#Squidward
s.create_rectangle(600,400,625,500, fill = "#0D47A1", outline = "black", width = 2)
s.create_rectangle(450,400,425,500, fill = "#0D47A1", outline = "black", width = 2)
s.create_polygon(625,500,620,505,430,505,425,500,fill = "#000234", outline = "black", width = 2)
s.create_polygon(435,650,450,300,600,300,615,650, fill = "#0D47A1",outline = "black", width = 2)
s.create_rectangle(465,375,585,400, fill = "#0D47A1", outline = "black", width = 2)
s.create_polygon(465,400,585,400,580,405,470,405, fill = "#000234", outline = "black", width = 2)
s.create_oval(465,400,510,440, fill = "#317FFF",outline = "black", width = 2)
s.create_oval(472,407,503,433, fill = "#C4DDF2",outline = "black", width = 1.6)
s.create_oval(585,400,540,440, fill = "#317FFF",outline = "black", width = 2)
s.create_oval(578,407,547,433, fill = "#C4DDF2",outline = "black", width = 1.6)
s.create_polygon(510,400,540,400,550,500,500,500, fill = "#0D47A1",outline = "black", width = 2)
s.create_polygon(550,500,545,505,505,505,500,500, fill = "#000234", outline = "black", width = 2)
s.create_oval(500,550,550,600, fill = "saddlebrown",outline = "#000234", width = 2)
s.create_rectangle(500,575,550,650, fill = "saddlebrown",  outline = "saddlebrown")
s.create_line(500,650,500,575,fill = "#000234", width = 2)
s.create_line(550,650,550,575,fill = "#000234", width = 2)
s.create_line(512.5,650,512.5,555.6, fill = "#412C1C", width = 2)
s.create_line(525,650,525,551.9, fill = "#412C1C", width = 2)
s.create_line(537.5,650,537.5,555.6, fill = "#412C1C", width = 2)
s.create_oval(537.5,600,550,612, fill = "orange")

#Spongebob
s.create_oval(750,400,950,600,fill = "orange", outline = "black",width = 2)
s.create_rectangle(750,500,950,650, fill = "orange")
s.create_line(750,500,750,650,950,650,950,500, fill = "black", width = 2)
s.create_polygon(815,475,750,350,800,250, fill = "green", smooth = True,outline = "black", width = 2)
s.create_polygon(885,475,950,350,900,250,fill = "green", smooth = True,outline = "black", width = 2)
s.create_polygon(850,480,785,360,850,225,915,360,fill = "green", smooth = True,outline = "black", width = 2)
s.create_line(950,500,900,550,750,650, fill = "brown",width = 2, smooth = True)
s.create_line(950,590,915,625,850,650,fill = "brown",width = 2, smooth = True)
s.create_line(924,435,850,510,750,575,fill = "brown",width = 2, smooth = True)
s.create_line(774,435,850,510,950,575,fill = "brown",width = 2, smooth = True)
s.create_line(750,590,785,635,850,650,fill = "brown",width = 2, smooth = True)
s.create_line(750,500,800,550,950,650,fill = "brown",width = 2, smooth = True)
s.create_oval(900,550,950,600,fill = "#317FFF",outline = "black", width = 2)
s.create_oval(907,557,943,593,fill = "#C4DDF2",outline = "black", width = 1.6)
s.create_oval(750,500,800,550,fill = "#317FFF",outline = "black", width = 2)
s.create_oval(757,507,793,543,fill = "#C4DDF2",outline = "black", width = 1.6)
s.create_oval(800,537.5,875,612.5,fill = "#317FFF",outline = "black", width = 2)
s.create_rectangle(800,575,875,650,fill = "#317FFF")
s.create_line(800,575,800,650,fill = "black", width = 2)
s.create_line(875,575,875,650,fill = "black", width = 2)
s.create_line(837.5,562.5,837.5,612.5, fill = "black", width = 2)
s.create_line(812.5,587.5,862.5,587.5, fill = "black", width = 2)
s.create_oval(825,575,850,600,fill = "#317FFF",outline = "black", width = 2)
s.create_rectangle(900,475,950,500,fill = "#81BFF4",outline = "black", width = 2)
s.create_rectangle(925,450,950,500,fill = "#81BFF4",outline = "black", width = 2)
s.create_line(922,450,953,450,fill = "#81BFF4", width = 10)

#roads
s.create_rectangle(800,650,875,855,fill = "grey",outline = "black", width = 2)
s.create_rectangle(500,650,550,855,fill = "grey",outline = "black", width = 2)
s.create_rectangle(0,825,2000,2000, fill = "grey")

#loops
for b in range(1,25):
    x = randint(922,953)
    y = randint(300,430)
    x2 = randint(1,5)
    y2 = x2
    s.create_oval(x,y,x+x2,y+x2, fill = "#317FFF", outline = "white", width = 1)
for r in range(1,20):
    x3 = randint(800,845)
    y3 = randint(650,800)
    x4 = randint(20,30)
    y4 = randint(20,25)
    s.create_oval(x3,y3,x3+x4,y3+y4,fill = "#C7F481", outline = "white", width = 1)



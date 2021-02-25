# Import module  
from tkinter import *
import tkinter
  
# Create object  
root = Tk() 
  
# Adjust size  
root.geometry("1000x600") 
root.resizable(0,0)

# Create Canvas 
canvas1 = Canvas( root, width = 800, height = 600) 
canvas1.pack(fill = "both", expand = True) 


# # #Function

def remove(event):
    canvas1.delete("remove")
    canvas1.delete("delete")
    canvas1.move("welcome", 0, 100)


def startNew(event):
    canvas1.create_rectangle(0, 0, 1000, 600, fill="white", tags="remove")



def quitNew(event):
    canvas1.move("welcome", 0, -100)
    canvas1.create_rectangle(300, 100, 700, 500, fill="white", tags="delete")
    canvas1.create_text(680, 120, text = "X", fill="black", font="Times 25 italic bold", tags="remove")
    canvas1.create_text(350, 130, anchor=W, font="Purisa",text="Most relationships seem so transitory")


# def start():
# canvas1.delete("bg1")
# Add image file 
bg = PhotoImage(file = "bgimage.gif") 


# Display image 
canvas1.create_image( 0, 0, image = bg, anchor = "nw") 

# Add Text 
canvas1.create_text(500, 150, text = "Start game!!!", fill="blue", font="Times 35 italic bold", tags="welcome")

#Button START
canvas1.create_rectangle(430, 220, 610, 280, fill="white", tags="start")
canvas1.create_text(515, 250, text = "Start", fill="black", font="Times 35 italic bold", tags="start")
canvas1.tag_bind("start", "<Button-1>", startNew)
#Button QUIT

canvas1.create_rectangle(430, 420, 610, 480, fill="white", tags="quit")
canvas1.create_text(515, 450, text = "Quit", fill="black", font="Times 35 italic bold", tags="quit")
canvas1.tag_bind("quit", "<Button-1>", quitNew)

canvas1.tag_bind("remove", "<Button-1>", remove)





# bg1 = PhotoImage(file = "bgimage.gif") 
# canvas1.create_image( 0, 0, image = bg1, anchor = "nw", tags="bg1")



# Display root 
root.mainloop()

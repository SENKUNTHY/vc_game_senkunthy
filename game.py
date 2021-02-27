# Import module  
from tkinter import *
  
# Create object  
root = Tk() 
grassImage = PhotoImage(file="grass.png")
grassImageHeight = grassImage.height()
grassImageWidth = grassImage.width()  
# ENEMY
enemyImage=PhotoImage(file="testenemy.png")
#PLAYER
playerImage=PhotoImage(file="testplayer.png")

#ARRAY2D
array=[
    ["w","w","W","w","w","W","w","w","W","w"],
    ["W","0","0","0","0","0","0","0","0","w"],
    ["W","0","0","0","E","0","0","0","0","w"],
    ["W","0","0","w","w","w","0","0","0","w"],
    ["W","0","0","0","0","0","0","0","E","w"],
    ["W","0","0","0","0","0","0","w","w","w"],
    ["W","P","0","0","0","0","0","0","0","w"],
    ["w","w","W","w","w","W","w","w","W","w"]
]

screenHeight = grassImageHeight*len(array)
screenWidth = grassImageWidth*len(array[0])
print(screenWidth, screenHeight)

root.geometry = (str(screenHeight)+"x"+str(screenWidth))
# Create Canvas 
canvas1 = Canvas( root, width = 800, height = 600) 
canvas1.pack(fill = "both", expand = True) 


# TESTING ARRAY2D

def drawGrid():
    global array, grassImage
    for row in range(len(array)):
        for col in range(len(array[row])):
            if array[row][col]=="w" or array[row][col]=="W":
                canvas1.create_image(grassImageWidth*col + grassImageWidth/2, grassImageHeight*row+grassImageHeight/2, image = grassImage)
            if array[row][col]=="E":
                canvas1.create_image(grassImageWidth*col + grassImageWidth/2, grassImageHeight*row+grassImageHeight/2, image = enemyImage)
            if array[row][col]=="P":
                canvas1.create_image(grassImageWidth*col + grassImageWidth/2, grassImageHeight*row+grassImageHeight/2, image = playerImage)


## #Function

def remove(event):
    canvas1.delete("remove")
    canvas1.delete("delete")
    canvas1.move("welcome", 0, 100)


def startNew(event):
    canvas1.delete("all")
    drawGrid()
    # canvas1.create_rectangle(0, 0, 1000, 600, fill="white", tags="remove")



def quitNew(event):
    canvas1.move("welcome", 0, -100)
    canvas1.create_rectangle(300, 100, 700, 500, fill="white", tags="delete")
    canvas1.create_text(680, 120, text = "X", fill="black", font="Times 25 italic bold", tags="remove")
    canvas1.create_text(350, 130, anchor=W, font="Purisa",text="Most relationships seem so transitory")


# def start():
# canvas1.delete("bg1")
# Add image file 
bg = PhotoImage(file = "bg.png")


# Display image 
canvas1.create_image( 0, 0, image = bg, anchor = "nw") 

# Add Text 
canvas1.create_text(500, 150, text = "Start game!!!", fill="white", font="Times 35 italic bold", tags="welcome")

#Button START
canvas1.create_rectangle(430, 220, 610, 280, fill="white", tags="start")
canvas1.create_text(515, 250, text = "Start", fill="black", font="Times 35 italic bold", tags="start")
canvas1.tag_bind("start", "<Button-1>", startNew)
#Button QUIT

canvas1.create_rectangle(430, 420, 610, 480, fill="white", tags="quit")
canvas1.create_text(515, 450, text = "Quit", fill="black", font="Times 35 italic bold", tags="quit")
canvas1.tag_bind("quit", "<Button-1>", quitNew)

canvas1.tag_bind("remove", "<Button-1>", remove)





# bg1 = PhotoImage(file = "bg.png") 
# canvas1.create_image( 0, 0, image = bg1, anchor = "nw", tags="bg1")



# Display root 
root.mainloop()

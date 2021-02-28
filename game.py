# Import module  
from tkinter import *
  
# Create object  
root = Tk() 
wallImage = PhotoImage(file="best.png")
wallImageHeight = wallImage.height()
wallImageWidth = wallImage.width()  
# ENEMY
enemyImage=PhotoImage(file="testenemy.png")
#PLAYER
playerImage=PhotoImage(file="testplayer.png")



#ARRAY2D
array=[
    ["w","w","w","W","w","w","W","w","w","W","w","w","w","w","w","w"],
    ["W","0","0","0","0","0","0","0","0","0","0","0","0","0","0","w"],
    ["W","0","0","0","0","E","0","0","0","0","0","0","0","0","0","w"],
    ["W","0","0","0","w","w","w","0","0","0","0","0","0","0","0","w"],
    ["W","0","0","0","0","0","0","0","0","E","0","0","0","0","0","w"],
    ["W","0","0","0","0","0","0","0","w","w","0","0","0","0","0","w"],
    ["W","0","0","0","0","0","0","0","0","0","0","0","0","0","0",'w'],
    ["W","0","0","0","0","0","0","0","0","0","0","0","0","0","E",'w'],
    ["W","P","0","0","0","0","0","0","0","0","0","0","0","w","w",'w'],
    ["w","w","w","W","w","w","W","w","w","W","w","w","w","w","w",'w']
]

positionPlayer = []

screenHeight = wallImageHeight*len(array)
screenWidth = wallImageWidth*len(array[0])
print(screenWidth, screenHeight)

root.geometry = (str(screenHeight)+"x"+str(screenWidth))
# Create Canvas 
canvas = Canvas( root, width =screenWidth, height = screenHeight) 
canvas.pack(fill = "both", expand = True) 


# TESTING ARRAY2D
def playerRight(event):
    global array, positionPlayer
    position = []
    for n in range(len(array)):
        for index in  range(len(array[n])):
            if array[n][index]  == "P":
                position.append(index)
                position.append(n)
    if array[position[1]][position[0]+1] == "0":
        array[position[1]][position[0]+1] = "P"
        array[position[1]][position[0]] = "0"
    canvas.delete("player")
    for row in range(len(array)):
        for col in range(len(array[row])):
            if array[row][col]=="w" or array[row][col]=="W":
                canvas.create_image(wallImageWidth*col + wallImageWidth/2, wallImageHeight*row+wallImageHeight/2, image = wallImage)
            if array[row][col]=="E":
                canvas.create_image(wallImageWidth*col + wallImageWidth/2, wallImageHeight*row+wallImageHeight/2, image = enemyImage)
            if array[row][col]=="P":
                canvas.create_image(wallImageWidth*col + wallImageWidth/2, wallImageHeight*row+wallImageHeight/2, image = playerImage, tags="player")

def playerLeft(event):
    global array, positionPlayer
    position = []
    for n in range(len(array)):
        for index in  range(len(array[n])):
            if array[n][index]  == "P":
                position.append(index)
                position.append(n)
    if array[position[1]][position[0]-1] == "0":
        array[position[1]][position[0]-1] = "P"
        array[position[1]][position[0]] = "0"
    canvas.delete("player")
    for row in range(len(array)):
        for col in range(len(array[row])):
            if array[row][col]=="w" or array[row][col]=="W":
                canvas.create_image(wallImageWidth*col + wallImageWidth/2, wallImageHeight*row+wallImageHeight/2, image = wallImage)
            if array[row][col]=="E":
                canvas.create_image(wallImageWidth*col + wallImageWidth/2, wallImageHeight*row+wallImageHeight/2, image = enemyImage)
            if array[row][col]=="P":
                canvas.create_image(wallImageWidth*col + wallImageWidth/2, wallImageHeight*row+wallImageHeight/2, image = playerImage, tags="player")

def playerUp(event):
    global array, positionPlayer
    position = []
    for n in range(len(array)):
        for index in  range(len(array[n])):
            if array[n][index]  == "P":
                position.append(index)
                position.append(n)
    if array[position[1]-1][position[0]] == "0":
        array[position[1]-1][position[0]] = "P"
        array[position[1]][position[0]] = "0"
    canvas.delete("player")
    for row in range(len(array)):
        for col in range(len(array[row])):
            if array[row][col]=="w" or array[row][col]=="W":
                canvas.create_image(wallImageWidth*col + wallImageWidth/2, wallImageHeight*row+wallImageHeight/2, image = wallImage)
            if array[row][col]=="E":
                canvas.create_image(wallImageWidth*col + wallImageWidth/2, wallImageHeight*row+wallImageHeight/2, image = enemyImage)
            if array[row][col]=="P":
                canvas.create_image(wallImageWidth*col + wallImageWidth/2, wallImageHeight*row+wallImageHeight/2, image = playerImage, tags="player")

def playerDown(event):
    global array, positionPlayer
    position = []
    for n in range(len(array)):
        for index in  range(len(array[n])):
            if array[n][index]  == "P":
                position.append(index)
                position.append(n)
    if array[position[1]+1][position[0]] == "0":
        array[position[1]+1][position[0]] = "P"
        array[position[1]][position[0]] = "0"
    canvas.delete("player")
    for row in range(len(array)):
        for col in range(len(array[row])):
            if array[row][col]=="w" or array[row][col]=="W":
                canvas.create_image(wallImageWidth*col + wallImageWidth/2, wallImageHeight*row+wallImageHeight/2, image = wallImage)
            if array[row][col]=="E":
                canvas.create_image(wallImageWidth*col + wallImageWidth/2, wallImageHeight*row+wallImageHeight/2, image = enemyImage)
            if array[row][col]=="P":
                canvas.create_image(wallImageWidth*col + wallImageWidth/2, wallImageHeight*row+wallImageHeight/2, image = playerImage, tags="player")

def drawGrid():
    global array, wallImage, positionPlayer
    canvas.create_image( 0, 0, image = bg, anchor = "nw") 
    for row in range(len(array)):
        for col in range(len(array[row])):
            if array[row][col]=="w" or array[row][col]=="W":
                canvas.create_image(wallImageWidth*col + wallImageWidth/2, wallImageHeight*row+wallImageHeight/2, image = wallImage)
            if array[row][col]=="E":
                canvas.create_image(wallImageWidth*col + wallImageWidth/2, wallImageHeight*row+wallImageHeight/2, image = enemyImage)
            if array[row][col]=="P":
                canvas.create_image(wallImageWidth*col + wallImageWidth/2, wallImageHeight*row+wallImageHeight/2, image = playerImage, tags="player")
            positionPlayer.append(wallImageWidth*col + wallImageWidth/2)
            positionPlayer.append(wallImageHeight*row+wallImageHeight/2)

## #Function

def remove(event):
    canvas.delete("remove")
    canvas.delete("delete")
    canvas.move("welcome", 0, 100)


def startNew(event):
    canvas.delete("all")
    drawGrid()
    # canvas.create_rectangle(0, 0, 1000, 600, fill="white", tags="remove")



def quitNew(event):
    canvas.move("welcome", 0, -100)
    canvas.create_rectangle(300, 100, 700, 500, fill="white", tags="delete")
    canvas.create_text(680, 120, text = "X", fill="black", font="Times 25 italic bold", tags="remove")
    canvas.create_text(350, 130, anchor=W, font="Purisa",text="Quit Game")

#Function move player
# def moveUp():
    
# Add image file 
bg = PhotoImage(file = "bg.png")


# Display image 
canvas.create_image( 0, 0, image = bg, anchor = "nw") 

# Add Text 
canvas.create_text(500, 150, text = "Start game!!!", fill="white", font="Times 35 italic bold", tags="welcome")

#Button START
canvas.create_rectangle(430, 220, 610, 280, fill="white", tags="start")
canvas.create_text(515, 250, text = "Start", fill="black", font="Times 35 italic bold", tags="start")
canvas.tag_bind("start", "<Button-1>", startNew)
#Button QUIT

canvas.create_rectangle(430, 420, 610, 480, fill="white", tags="quit")
canvas.create_text(515, 450, text = "Quit", fill="black", font="Times 35 italic bold", tags="quit")
canvas.tag_bind("quit", "<Button-1>", quitNew)

canvas.tag_bind("remove", "<Button-1>", remove)


root.bind("<Right>", playerRight)
root.bind("<Left>", playerLeft)
root.bind("<Up>", playerUp)
root.bind("<Down>", playerDown)
#BUTTON FOR MOVE PLAYER
# root.bind("<Up>", moveUp) #Move up
# root.bind("<Down>", moveDown)  #Move down



# Display root 
root.mainloop()

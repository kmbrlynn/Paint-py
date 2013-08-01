# Kmbrlynn
# July 2013
# Simple GUI paint app built with Python

# =========================================================


from Tkinter import *

# random var for testing

foo = 3


# this will hold a pressed or released value
mouseState = "up"

# this will hold the x or y value of the cursor. null if not pressed
xState = None       
yState = None

def main():
    root = Tk()
    root.wm_title("Paint!")
    
    # define screen dimensions for responsiveness
    screen_width = root.winfo_screenwidth()         
    screen_height = root.winfo_screenheight()
    # set the window size
    root.minsize(screen_width/2, screen_height/2)
    
    # create a canvas
    myCanvas = Canvas(root)
    # fit the canvas to the window. width and height are built into Tkinter
    myCanvas.config(width = screen_width/2, height = screen_height/2)
    
    # create a button for blue
    blueButton = Button(root, text ="Blue", command = bluePressed)
    
    # this packs widgets into rows and columns
    myCanvas.pack()
    blueButton.pack()
    
    # bind my functions to built-in Tkinter mouse events
    myCanvas.bind("<Motion>", moveMouse)
    myCanvas.bind("<ButtonPress-1>", press)
    myCanvas.bind("<ButtonRelease-1>", release)
    root.mainloop()

# function for when mouse is in pressed position
def press(event):
    # don't forget to include global vars in your function
    global mouseState
    mouseState = "down"

# function for when you move the mouse
def moveMouse(event):
    # essentially, if press() is true...
    if mouseState == "down":
        global xState
        global yState
        # ...and xState and yState are null - aka release() is NOT true, 
        if xState is not None and yState is not None:
            event.widget.create_line(xState,yState,event.x,event.y,smooth=TRUE)
        # then populate xState and yState with the coords of the mouse position - aka draw :)
        xState = event.x
        yState = event.y

# function for when mouse is in released position
def release(event):
    global mouseState
    global xState
    global yState
    mouseState = "up"
    # reset the line when you let go of the button
    xState = None           
    yState = None

# function for when you press the blue button
def bluePressed():
    foo = 5
    print("blue clicked")

if __name__ == "__main__":
    main()

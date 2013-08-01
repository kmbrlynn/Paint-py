# Kmbrlynn
# July 2013
# Simple GUI paint app built with Python

# =========================================================


from Tkinter import *

# this will hold a pressed or released value
mouseState = "up"

# null value will pass thru these on release, making the draw not happen
xOnRelease = None       
yOnRelease = None

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
    
    # this packs widgets into rows and columns
    myCanvas.pack()
    # bind my functions to built-in Tkinter mouse events
    myCanvas.bind("<Motion>", moveMouse)
    myCanvas.bind("<ButtonPress-1>", press)
    myCanvas.bind("<ButtonRelease-1>", release)
    root.mainloop()

def press(event):
    # don't forget to include global vars in your function
    global mouseState       
    mouseState = "down"           

def release(event):
    global mouseState, xOnRelease, yOnRelease       
    mouseState = "up"
    # reset the line when you let go of the button
    xOnRelease = None           
    yOnRelease = None

def moveMouse(event):
    if mouseState == "down":
        global xOnRelease, yOnRelease
        # detect whether or not the mouse is pressed
        if xOnRelease is not None and yOnRelease is not None:
            event.widget.create_line(xOnRelease,yOnRelease,event.x,event.y,smooth=TRUE)
        # draw it! :)
        xOnRelease = event.x
        yOnRelease = event.y

if __name__ == "__main__":
    main()

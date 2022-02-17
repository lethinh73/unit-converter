import tkinter
from functions import *
from PIL import Image, ImageTk

# Create the main window
theApp = tkinter.Tk()
canvas = tkinter.Canvas(theApp, width=800, height=500, bg=('#470D21'))
canvas.grid(columnspan=3)

# Insert team logo at the corner of the window
teamLogo = Image.open("logo.png")
teamLogo = teamLogo.resize((100, 30), Image.ANTIALIAS)
teamLogo = ImageTk.PhotoImage(teamLogo)
canvas.create_image(750, 485, image=teamLogo)


# Main Application Loop
theApp.mainloop()
import functools
import tkinter
from functions import *

# Create the main window
theApp = tkinter.Tk()
canvas = tkinter.Canvas(theApp, width=800, height=500)
canvas.grid(columnspan=3)

# Main Application Loop
theApp.mainloop()
from functions import *
from tkinter import *

mainApp = Tk()

# Set title and size for the window
mainApp.title("Team Speak - Unit Converter/Calculator")
mainApp.geometry("500x650")

# App background
mainApp.configure(background="#94B49F")

# App title
appTitle = Label(
    mainApp, text="Unit Converter and Calculator", fg="#362706", bg="#94B49F"
)
appTitle.config(font=("Arial", 30))
appTitle.pack(pady=20)
mainApp.mainloop()

from turtle import bgcolor
from black import main
from click import style
from functions import *
from tkinter import Label, ttk, Tk

mainApp = Tk()
tabControl = ttk.Notebook(mainApp)

# Set title and size for the window
mainApp.title("Team Speak - Unit Converter/Calculator")
mainApp.geometry("500x650")

# App title
appTitle = Label(mainApp, text="Unit Converter and Calculator", fg="white")
appTitle.config(font=("Arial", 30))
appTitle.pack(pady=20)

# Create 2 tabs
tabConverter = ttk.Frame(tabControl)
tabCalculator = ttk.Frame(tabControl)
tabControl.add(tabConverter, text="Number Converting")
tabControl.add(tabCalculator, text="Calculator")
tabControl.pack(expand=1, fill="both")

# Tab Converter
text = Label(tabConverter, text="Hello", fg="white")
text.pack(side="left", ipadx=10)
# Tab Calculator

mainApp.mainloop()

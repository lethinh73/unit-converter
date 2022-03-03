from tkinter.font import BOLD
from functions import *
from tkinter import *
from tkinter import ttk

mainApp = Tk()

# Set title and size for the window
mainApp.title("Team Speak")
mainApp.geometry("+250+250")

# App title
titleArea = Frame(mainApp, width=500, height=100, bg="lightgreen")
titleArea.grid(columnspan=3, column=0, row=0)
appTitle = Label(mainApp, text="Number Converter and Calculator",
                 fg="black", bg="lightgreen")
appTitle.config(font=("Arial", 20))
appTitle.grid(columnspan=3, row=0, column=0)

# Create 2 tabs
tabControl = ttk.Notebook(mainApp)
tabConverter = ttk.Frame(tabControl, height=500, width=500)
tabCalculator = ttk.Frame(tabControl, height=500, width=500)
tabControl.add(tabConverter, text="Number Converting")
tabControl.add(tabCalculator, text="Calculator")
tabControl.grid(columnspan=3, row=1, column=0)

# Tab Converter
randomColors = ["pink", "yellow", "orange", "red", "cyan",
                "blue", "violet", "lightblue", "green", "gray"]
ConverterArea = Frame(tabConverter, width=500, height=500, bg="blue")
ConverterArea.grid(column=0, row=0, columnspan=10, rowspan=10)
for i in range(0, 10):
    for j in range(0, 10):
        Label(tabConverter, text=f"{i}x{j}",
              fg="black", bg=randomColors[i]).grid(row=i, column=j)

# Tab Calculator
CalculatorArea = Frame(tabCalculator, width=500, height=500, bg="cyan")
CalculatorArea.grid(column=0, row=0, columnspan=3, rowspan=10)

mainApp.mainloop()

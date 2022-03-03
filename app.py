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
tabControl.add(tabCalculator, text="Binary Calculator")
tabControl.grid(columnspan=3, row=1, column=0)

# Tab Converter
randomColors = ["pink", "yellow", "orange", "red", "cyan",
                "blue", "violet", "lightblue", "green", "gray"]
ConverterArea = Frame(tabConverter, width=500, height=400, bg="blue")
ConverterArea.grid(column=0, row=0, columnspan=3, rowspan=10)

# Tab Calculator
tabCalColor = "cyan"
CalculatorArea = Frame(tabCalculator, width=500, height=400, bg=tabCalColor)
CalculatorArea.grid(column=0, row=0, columnspan=3, rowspan=10)

CalTitle = Label(tabCalculator, text="Binary Calculator", bg=tabCalColor)
CalTitle.grid(column=0, row=0, columnspan=3)

num1Label = Label(tabCalculator, text="Number 1:", bg=tabCalColor)
num1Label.grid(column=0, row=1)
num1Entry = Entry(tabCalculator, width=25)
num1Entry.grid(column=1, row=1, sticky="w")
num1ClearBtn = Button(tabCalculator, width=15, text="Clear")
num1ClearBtn.grid(column=2, row=1, sticky="w")

num2Label = Label(tabCalculator, text="Number 2:", bg=tabCalColor)
num2Label.grid(column=0, row=2)
num2Entry = Entry(tabCalculator, width=25)
num2Entry.grid(column=1, row=2, sticky="w")
num2ClearBtn = Button(tabCalculator, width=15, text="Clear")
num2ClearBtn.grid(column=2, row=2, sticky="w")

resultLabel = Label(tabCalculator, height=5,
                    text="Result: ________ ", bg=tabCalColor)
resultLabel.grid(column=1, row=3, sticky="w")

# Calculation buttons
addBtn = Button(tabCalculator, width=15, text="ADD")
addBtn.grid(column=0, row=4)
subBtn = Button(tabCalculator, width=15, text="SUBTRACT")
subBtn.grid(column=1, row=4)
mulBtn = Button(tabCalculator, width=15, text="MULTIPLY")
mulBtn.grid(column=2, row=4)
devBtn = Button(tabCalculator, width=15, text="DEVIDE")
devBtn.grid(column=0, row=5)
andBtn = Button(tabCalculator, width=15, text="AND")
andBtn.grid(column=1, row=5)
orBtn = Button(tabCalculator, width=15, text="OR")
orBtn.grid(column=2, row=5)
xorBtn = Button(tabCalculator, width=15, text="XOR")
xorBtn.grid(column=0, row=6)
notBtn = Button(tabCalculator, width=15, text="NOT")
notBtn.grid(column=1, row=6)
norBtn = Button(tabCalculator, width=15, text="NOR")
norBtn.grid(column=2, row=6)

mainApp.mainloop()

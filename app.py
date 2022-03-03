from tkinter import *
from tkinter import ttk
from tkinter import font
from functions import *

mainApp = Tk()

# App events
# ------------------------------------------------------------ #


# Clear entry number 1
def clearNum1():
    num1Entry.delete(0, END)


# Clear entry number 1
def clearNum2():
    num2Entry.delete(0, END)


# "ADD" button clicked event
def addBtnClicked():
    try:
        result = add_binary(num1Entry.get(), num2Entry.get())
        resultLabel.config(text="Result: " + result)
    except:
        resultLabel.config(text="Error! Please check your input!")


# "SUBTRACT" button clicked event
def subBtnClicked():
    try:
        result = sub_binary(num1Entry.get(), num2Entry.get())
        resultLabel.config(text="Result: " + result)
    except:
        resultLabel.config(text="Error! Please check your input!")


# "MULTIPLY" button clicked event
def mulBtnClicked():
    try:
        result = mul_binary(num1Entry.get(), num2Entry.get())
        resultLabel.config(text="Result: " + result)
    except:
        resultLabel.config(text="Error! Please check your input!")


# "DEVIDE" button clicked event
def devBtnClicked():
    resultLabel.config(text="WORKING ON IT!!!")


# "AND" button clicked event
def andBtnClicked():
    try:
        result = and_binary(num1Entry.get(), num2Entry.get())
        resultLabel.config(text="Result: " + result)
    except:
        resultLabel.config(text="Error! Please check your input!")


# "OR" button clicked event
def orBtnClicked():
    try:
        result = or_binary(num1Entry.get(), num2Entry.get())
        resultLabel.config(text="Result: " + result)
    except:
        resultLabel.config(text="Error! Please check your input!")


# "XOR" button clicked event
def xorBtnClicked():
    try:
        result = xor_binary(num1Entry.get(), num2Entry.get())
        resultLabel.config(text="Result: " + result)
    except:
        resultLabel.config(text="Error! Please check your input!")


# "NOT" button clicked event
def notBtnClicked():
    try:
        result = not_binary(num1Entry.get())
        resultLabel.config(text="Result (for Number 1): " + result)
    except:
        resultLabel.config(text="Error! Please check your input!")


# "NOR" button clicked event
def norBtnClicked():
    resultLabel.config(text="WORKING ON IT!!!")

# ------------------------------------------------------------ #


# App settings
titleBackColor = "#222831"
tabCalColor = "#EEEEEE"
tabConColor = "#EEEEEE"

# Set title and size for the window
mainApp.title("Team Speak")
mainApp.resizable(0, 0)
mainApp.geometry("+250+250")

# App title
titleArea = Frame(mainApp, width=500, height=100, bg=titleBackColor)
titleArea.grid(columnspan=3, column=0, row=0)
appTitle = Label(mainApp, text="Number Converter and Calculator",
                 fg="white", bg=titleBackColor)
appTitle.config(font=("Arial", 20, font.BOLD))
appTitle.grid(columnspan=3, row=0, column=0)

# Create 2 tabs
tabControl = ttk.Notebook(mainApp)
tabConverter = ttk.Frame(tabControl, height=500, width=500)
tabCalculator = ttk.Frame(tabControl, height=500, width=500)
tabControl.add(tabConverter, text="Conversion")
tabControl.add(tabCalculator, text="Calculation")
tabControl.grid(columnspan=3, row=1, column=0)

# Tab Converter
ConverterArea = Frame(tabConverter, width=500, height=400, bg=tabConColor)
ConverterArea.grid(column=0, row=0, columnspan=3, rowspan=10)

# Tab Calculator
CalculatorArea = Frame(tabCalculator, width=500, height=400, bg=tabCalColor)
CalculatorArea.grid(column=0, row=0, columnspan=3, rowspan=10)

CalTitle = Label(tabCalculator, text="Binary Calculator", bg=tabCalColor)
CalTitle.config(font=("Arial", 15))
CalTitle.grid(column=0, row=0, columnspan=3)

num1Label = Label(tabCalculator, text="Number 1:", bg=tabCalColor)
num1Label.grid(column=0, row=1)
num1Entry = Entry(tabCalculator, width=25)
num1Entry.grid(column=1, row=1, sticky="w")
num1ClearBtn = Button(tabCalculator, width=15, text="Clear", command=clearNum1)
num1ClearBtn.grid(column=2, row=1, sticky="w")

num2Label = Label(tabCalculator, text="Number 2:", bg=tabCalColor)
num2Label.grid(column=0, row=2)
num2Entry = Entry(tabCalculator, width=25)
num2Entry.grid(column=1, row=2, sticky="w")
num2ClearBtn = Button(tabCalculator, width=15, text="Clear", command=clearNum2)
num2ClearBtn.grid(column=2, row=2, sticky="w")

resultLabel = Label(tabCalculator, text="", bg=tabCalColor)
resultLabel.config(font=("Arial", 15, font.BOLD))
resultLabel.grid(column=0, columnspan=3, row=3)

# Calculation buttons
addBtn = Button(tabCalculator, width=15, text="ADD", command=addBtnClicked)
addBtn.grid(column=0, row=4)
subBtn = Button(tabCalculator, width=15,
                text="SUBTRACT", command=subBtnClicked)
subBtn.grid(column=1, row=4)
mulBtn = Button(tabCalculator, width=15,
                text="MULTIPLY", command=mulBtnClicked)
mulBtn.grid(column=2, row=4)
devBtn = Button(tabCalculator, width=15, text="DEVIDE", command=devBtnClicked)
devBtn.grid(column=0, row=5)
andBtn = Button(tabCalculator, width=15, text="AND", command=andBtnClicked)
andBtn.grid(column=1, row=5)
orBtn = Button(tabCalculator, width=15, text="OR", command=orBtnClicked)
orBtn.grid(column=2, row=5)
xorBtn = Button(tabCalculator, width=15, text="XOR", command=xorBtnClicked)
xorBtn.grid(column=0, row=6)
notBtn = Button(tabCalculator, width=15, text="NOT", command=notBtnClicked)
notBtn.grid(column=1, row=6)
norBtn = Button(tabCalculator, width=15, text="NOR", command=norBtnClicked)
norBtn.grid(column=2, row=6)

mainApp.mainloop()

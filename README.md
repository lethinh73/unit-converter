# Unit Converter and Calculator

This is a University Software Engineering course project that combines a number converter and a calculator, supporting **Decimal**, **Binary (32-bit)**, and **Hexadecimal** formats.

---

## Team Members

* Jesse Lira
* Thinh Le
* Richard Trinh
* Sam Callaway

---

## Features

This application provides two main functionalities:

### Number Converter

* **Convert Numbers:** Easily convert numbers between Decimal, 32-bit Binary, and Hexadecimal formats.
* **IEEE 754 Representation Breakdown:** For binary conversions, the application displays the breakdown into **Sign**, **Exponent**, and **Mantissa** components.

### Calculator

Perform arithmetic and bitwise operations on two numbers, with input and output supporting Decimal, 32-bit Binary, and Hexadecimal formats.

* **Arithmetic Operations:**
    * Addition (`+`)
    * Subtraction (`-`)
    * Multiplication (`*`)
    * Division (`/`)
* **Bitwise Operations:**
    * AND (`&`)
    * OR (`|`)
    * XOR (`^`)
    * NOT (`~`)
    * Left Shift (`<<`)
    * Right Shift (`>>`)

---

## Technologies Used

* **Python 3:** The core programming language.
* **PyQt5:** Used for building the graphical user interface (GUI).
* **`struct` module:** Utilized for handling conversions between Python values and C structs (specifically for floating-point number representation).

---

## How to Run

1.  **Prerequisites:** Ensure you have **Python 3** installed on your system.
2.  **Install PyQt5:** If you don't have PyQt5 installed, you can install it via pip:
    ```bash
    pip install PyQt5
    ```
3.  **Clone the repository (or download the files):**
    ```bash
    git clone <your-repository-url>
    cd unit-converter
    ```
    (Replace `<your-repository-url>` with the actual URL of your repository.)
4.  **Run the application:**
    ```bash
    python app.py
    ```

---

## Usage

### Converter Tab

1.  Enter a number in the **"Number:"** input field.
2.  Select the **"Format:"** corresponding to the number you entered (Decimal, Binary (32-bit), or Hex).
3.  Click the **"CONVERT"** button.
4.  The converted values in Decimal, Binary, and Hexadecimal will be displayed in their respective fields. For binary, the Sign, Exponent, and Mantissa will also be shown.

### Calculator Tab

1.  Enter the first number in the **"Number 1:"** input field and select its format using the dropdown.
2.  Enter the second number in the **"Number 2:"** input field and select its format.
3.  Choose the desired operation by clicking one of the buttons (ADD, SUBTRACT, MULTIPLY, DIVIDE, AND, OR, XOR, NOT, LSHIFT, RSHIFT).
4.  Select the desired **"Result:"** format using the dropdown.
5.  The result of the operation will be displayed in the **"Result:"** field.
6.  Use the **"CLEAR"** buttons to clear the input fields for Number 1 and Number 2.

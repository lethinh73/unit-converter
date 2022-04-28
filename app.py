from PyQt5 import QtCore, QtGui, QtWidgets
from number import Number

# Global variables
options = {
    0: 'Decimal',
    1: 'Binary (32-bit)',
    2: 'Hex (8-bit)'
}

optionNum = 0
optionNum1 = 0
optionNum2 = 0
optionResult = 0

num = Number()
num1 = Number()
num2 = Number()
result = Number()


class Ui_MainWindow(object):
    ###########################################################################
    # APP EVENT FUNCTIONS
    ###########################################################################
    # App initialization
    def init(self):
        print('App initializing...')

        # Add options to option boxes:
        MainWindow.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.comboNum1.addItems(options.values())
        self.comboNum2.addItems(options.values())
        self.comboResult.addItems(options.values())
        self.comboNum.addItems(options.values())
        self.txtError.setText('')

        # Change color of output to gray
        self.txtBinary.setStyleSheet('background-color: #D3D3D3;')
        self.txtHex.setStyleSheet('background-color: #D3D3D3;')
        self.txtSem1.setStyleSheet('background-color: #D3D3D3;')
        self.txtSem2.setStyleSheet('background-color: #D3D3D3;')
        self.txtSem3.setStyleSheet('background-color: #D3D3D3;')
        self.txtDecimal.setStyleSheet('background-color: #D3D3D3;')
        self.txtResult.setStyleSheet('background-color: #D3D3D3;')

        # Set ouput textbox to 'read-only'
        self.txtBinary.setReadOnly(True)
        self.txtHex.setReadOnly(True)
        self.txtSem1.setReadOnly(True)
        self.txtSem2.setReadOnly(True)
        self.txtSem3.setReadOnly(True)
        self.txtDecimal.setReadOnly(True)
        self.txtResult.setReadOnly(True)

        # Set default tab when openning to 'Converter'
        self.tabWidget.setCurrentIndex(0)

        # Set fonts for option boxes
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboNum.setFont(font)
        self.comboNum1.setFont(font)
        self.comboNum2.setFont(font)
        self.comboResult.setFont(font)

        print('App initialized!')

    # ComboBox 'Number' changed
    def comboNumChanged(self):
        global optionNum
        optionNum = self.comboNum.currentIndex()
        print('Format option changed to: ', options[optionNum])

    # Button 'Convert' clicked
    def btnConvertClicked(self):
        global num
        self.txtError.setText('')
        print(f'Button Convert clicked with {options[optionNum]} option')

        try:
            if optionNum == 0:
                num.set_from_float(float(self.txtNum.text()))
                self.txtBinary.setText(str(num.get_bin()))
                self.txtHex.setText(str(num.get_hex()))
                self.txtDecimal.setText(str(num.get_float()))
                self.txtSem1.setText(num.get_bin()[0:1])
                self.txtSem2.setText(num.get_bin()[1:9])
                self.txtSem3.setText(num.get_bin()[9:32])
            elif optionNum == 1:
                num.set_from_bin(self.txtNum.text())
                self.txtBinary.setText(str(num.get_bin()))
                self.txtHex.setText(str(num.get_hex()))
                self.txtDecimal.setText(str(num.get_float()))
                self.txtSem1.setText(num.get_bin()[0:1])
                self.txtSem2.setText(num.get_bin()[1:9])
                self.txtSem3.setText(num.get_bin()[9:32])
            elif optionNum == 2:
                num.set_from_hex(self.txtNum.text())
                self.txtBinary.setText(str(num.get_bin()))
                self.txtHex.setText(str(num.get_hex()))
                self.txtDecimal.setText(str(num.get_float()))
                self.txtSem1.setText(num.get_bin()[0:1])
                self.txtSem2.setText(num.get_bin()[1:9])
                self.txtSem3.setText(num.get_bin()[9:32])
        except Exception as e:
            self.txtError.setText('Error! Please enter a valid number.')
            self.txtBinary.setText('')
            self.txtHex.setText('')
            self.txtSem1.setText('')
            self.txtSem2.setText('')
            self.txtSem3.setText('')
            self.txtDecimal.setText('')
            print('Error: ', e)

    # ComboBox 'Number 1' changed
    def comboNum1Changed(self):
        global optionNum1
        optionNum1 = self.comboNum1.currentIndex()
        print('Format option for Number 1 changed to: ', options[optionNum1])


    # ComboBox 'Number 2' changed
    def comboNum2Changed(self):
        global optionNum2
        optionNum2 = self.comboNum2.currentIndex()
        print('Format option for Number 2 changed to: ', options[optionNum2])

    # ComboBox 'Result' changed
    def comboResultChanged(self):
        global optionResult
        optionResult = self.comboResult.currentIndex()
        print('Format option for Result changed to: ', options[optionResult])

        if(self.txtResult.text() != ''):
            self.outputResult()

    # Input number 1
    def inputNum1(self):
        global num1, optionNum1
        print('Input number 1, with format: ', options[optionNum1])
        if optionNum1 == 0:
            num1.set_from_float(float(self.txtNum1.text()))
        elif optionNum1 == 1:
            num1.set_from_binary(self.txtNum1.text())
        elif optionNum1 == 2:
            num1.set_from_hex(self.txtNum1.text())
        elif optionNum1 == 3:
            num1.set_from_sem(self.txtNum1.text())

    # Input number 2
    def inputNum2(self):
        global num2, optionNum2
        print('Input number 2, with format: ', options[optionNum2])
        if optionNum2 == 0:
            num2.set_from_float(float(self.txtNum2.text()))
        elif optionNum2 == 1:
            num2.set_from_binary(self.txtNum2.text())
        elif optionNum2 == 2:
            num2.set_from_hex(self.txtNum2.text())
        elif optionNum2 == 3:
            num2.set_from_sem(self.txtNum2.text())

    # Output result
    def outputResult(self):
        global result, optionResult
        print('Output result, with format: ', options[optionResult])
        if optionResult == 0:
            self.txtResult.setText(str(result.get_float()))
        elif optionResult == 1:
            self.txtResult.setText(str(result.get_binary()))
        elif optionResult == 2:
            self.txtResult.setText(str(result.get_hex()))
        elif optionResult == 3:
            self.txtResult.setText(str(result.get_sem()))

    # Button 'Add' clicked
    def btnAddClicked(self):
        global result, num1, num2
        print('Button Add clicked')
        try:
            self.inputNum1()
            self.inputNum2()

            result = num1 + num2

            self.outputResult()
        except Exception as e:
            self.txtResult.setText('Error! Please enter a valid number.')
            print('Error: ', e)

    # Button 'Subtract' clicked
    def btnSubClicked(self):
        global result, num1, num2
        print('Button Subtract clicked')
        try:
            self.inputNum1()
            self.inputNum2()

            result = num1 - num2

            self.outputResult()
        except Exception as e:
            self.txtResult.setText('Error! Please enter a valid number.')
            print('Error: ', e)

    # Button 'Multiply' clicked
    def btnMulClicked(self):
        global result, num1, num2
        print('Button Multiply clicked')
        try:
            self.inputNum1()
            self.inputNum2()

            result = num1 * num2

            self.outputResult()
        except Exception as e:
            self.txtResult.setText('Error! Please enter a valid number.')
            print('Error: ', e)

    # Button 'Divide' clicked
    def btnDivClicked(self):
        global result, num1, num2
        print('Button Divide clicked')
        try:
            self.inputNum1()
            self.inputNum2()

            result = num1 / num2

            self.outputResult()
        except Exception as e:
            self.txtResult.setText('Error! Please enter a valid number.')
            print('Error: ', e)

    # Button 'AND' clicked
    def btnAndClicked(self):
        global result, num1, num2
        print('Button AND clicked')
        try:
            self.inputNum1()
            self.inputNum2()

            result = num1 & num2

            self.outputResult()
        except Exception as e:
            self.txtResult.setText('Error! Please enter a valid number.')
            print('Error: ', e)

    # Button 'OR' clicked
    def btnOrClicked(self):
        global result, num1, num2
        print('Button OR clicked')
        try:
            self.inputNum1()
            self.inputNum2()

            result = num1 | num2

            self.outputResult()
        except Exception as e:
            self.txtResult.setText('Error! Please enter a valid number.')
            print('Error: ', e)

    # Button 'XOR' clicked
    def btnXorClicked(self):
        global result, num1, num2
        print('Button XOR clicked')
        try:
            self.inputNum1()
            self.inputNum2()

            result = num1 ^ num2

            self.outputResult()
        except Exception as e:
            self.txtResult.setText('Error! Please enter a valid number.')
            print('Error: ', e)

    # Button 'NOT' clicked
    def btnNotClicked(self):
        global result, num1
        print('Button NOT clicked')
        try:
            self.inputNum1()

            result = ~num1

            self.txtNum2.setText('')

            self.outputResult()
        except Exception as e:
            self.txtResult.setText('Error! Please enter a valid number.')
            print('Error: ', e)

    # Button 'NOR' clicked
    def btnNorClicked(self):
        global result, num1, num2
        print('Button NOR clicked')
        try:
            self.inputNum1()
            self.inputNum2()

            result = ~(num1 | num2)

            self.outputResult()
        except Exception as e:
            self.txtResult.setText('Error! Please enter a valid number.')
            print('Error: ', e)

    # Button 'Left Shift' clicked
    def btnLshiftClicked(self):
        global result, num1, num2
        print('Button Left Shift clicked')
        try:
            self.inputNum1()
            self.inputNum2()

            result = num1 << num2

            self.outputResult()
        except Exception as e:
            self.txtResult.setText('Error! Please enter a valid number.')
            print('Error: ', e)

    # Button 'Right Shift' clicked
    def btnRshiftClicked(self):
        global result, num1, num2
        print('Button Right Shift clicked')
        try:
            self.inputNum1()
            self.inputNum2()

            result = num1 >> num2

            self.outputResult()
        except Exception as e:
            self.txtResult.setText('Error! Please enter a valid number.')
            print('Error: ', e)

    # Button 'LSHIFT' clicked
    def btnLShiftClicked(self):
        global result, num1, num2
        print('Button LSHIFT clicked')
        try:
            self.inputNum1()
            self.inputNum2()

            result = num1 << num2

            self.outputResult()
        except Exception as e:
            self.txtResult.setText('Error! Please enter a valid number.')
            print('Error: ', e)

    # Button 'RSHIFT' clicked
    def btnRShiftClicked(self):
        global result, num1, num2
        print('Button RSHIFT clicked')
        try:
            self.inputNum1()
            self.inputNum2()

            result = num1 >> num2

            self.outputResult()
        except Exception as e:
            self.txtResult.setText('Error! Please enter a valid number.')
            print('Error: ', e)

###########################################################################
# GENERATED GUI CODES
###########################################################################

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(5, 125, 790, 551))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tabConvert = QtWidgets.QWidget()
        self.tabConvert.setObjectName("tabConvert")
        self.label_6 = QtWidgets.QLabel(self.tabConvert)
        self.label_6.setGeometry(QtCore.QRect(300, 20, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.txtNum = QtWidgets.QLineEdit(self.tabConvert)
        self.txtNum.setGeometry(QtCore.QRect(110, 100, 365, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.txtNum.setFont(font)
        self.txtNum.setObjectName("txtNum")
        self.comboNum = QtWidgets.QComboBox(self.tabConvert)
        self.comboNum.setGeometry(QtCore.QRect(490, 100, 161, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.comboNum.setFont(font)
        self.comboNum.setCurrentText("")
        self.comboNum.setObjectName("comboNum")
        self.txtDecimal = QtWidgets.QLineEdit(self.tabConvert)
        self.txtDecimal.setEnabled(True)
        self.txtDecimal.setGeometry(QtCore.QRect(280, 180, 365, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.txtDecimal.setFont(font)
        self.txtDecimal.setObjectName("txtDecimal")
        self.txtBinary = QtWidgets.QLineEdit(self.tabConvert)
        self.txtBinary.setEnabled(True)
        self.txtBinary.setGeometry(QtCore.QRect(280, 250, 365, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.txtBinary.setFont(font)
        self.txtBinary.setObjectName("txtBinary")
        self.txtSem1 = QtWidgets.QLineEdit(self.tabConvert)
        self.txtSem1.setGeometry(QtCore.QRect(280, 320, 21, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.txtSem1.setFont(font)
        self.txtSem1.setText("")
        self.txtSem1.setObjectName("txtSem1")
        self.txtHex = QtWidgets.QLineEdit(self.tabConvert)
        self.txtHex.setGeometry(QtCore.QRect(280, 390, 365, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.txtHex.setFont(font)
        self.txtHex.setObjectName("txtHex")
        self.label_7 = QtWidgets.QLabel(self.tabConvert)
        self.label_7.setGeometry(QtCore.QRect(210, 180, 60, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tabConvert)
        self.label_8.setGeometry(QtCore.QRect(210, 250, 60, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tabConvert)
        self.label_9.setGeometry(QtCore.QRect(210, 320, 60, 20))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tabConvert)
        self.label_10.setGeometry(QtCore.QRect(210, 390, 60, 20))
        self.label_10.setObjectName("label_10")
        self.btnConvert = QtWidgets.QPushButton(self.tabConvert)
        self.btnConvert.setGeometry(QtCore.QRect(325, 460, 150, 30))
        self.btnConvert.setObjectName("btnConvert")
        self.txtError = QtWidgets.QLabel(self.tabConvert)
        self.txtError.setGeometry(QtCore.QRect(200, 135, 400, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txtError.setFont(font)
        self.txtError.setAlignment(QtCore.Qt.AlignCenter)
        self.txtError.setObjectName("txtError")
        self.label_12 = QtWidgets.QLabel(self.tabConvert)
        self.label_12.setGeometry(QtCore.QRect(110, 70, 75, 20))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tabConvert)
        self.label_13.setGeometry(QtCore.QRect(490, 70, 75, 20))
        self.label_13.setObjectName("label_13")
        self.txtSem2 = QtWidgets.QLineEdit(self.tabConvert)
        self.txtSem2.setGeometry(QtCore.QRect(330, 320, 101, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.txtSem2.setFont(font)
        self.txtSem2.setText("")
        self.txtSem2.setObjectName("txtSem2")
        self.txtSem3 = QtWidgets.QLineEdit(self.tabConvert)
        self.txtSem3.setGeometry(QtCore.QRect(460, 320, 261, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.txtSem3.setFont(font)
        self.txtSem3.setText("")
        self.txtSem3.setObjectName("txtSem3")
        self.label_11 = QtWidgets.QLabel(self.tabConvert)
        self.label_11.setGeometry(QtCore.QRect(270, 350, 41, 20))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_14 = QtWidgets.QLabel(self.tabConvert)
        self.label_14.setGeometry(QtCore.QRect(330, 350, 101, 20))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tabConvert)
        self.label_15.setGeometry(QtCore.QRect(460, 350, 261, 20))
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.tabWidget.addTab(self.tabConvert, "")
        self.tabCalculate = QtWidgets.QWidget()
        self.tabCalculate.setObjectName("tabCalculate")
        self.txtNum1 = QtWidgets.QLineEdit(self.tabCalculate)
        self.txtNum1.setGeometry(QtCore.QRect(150, 90, 365, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.txtNum1.setFont(font)
        self.txtNum1.setObjectName("txtNum1")
        self.txtNum2 = QtWidgets.QLineEdit(self.tabCalculate)
        self.txtNum2.setGeometry(QtCore.QRect(150, 160, 365, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.txtNum2.setFont(font)
        self.txtNum2.setObjectName("txtNum2")
        self.label_2 = QtWidgets.QLabel(self.tabCalculate)
        self.label_2.setGeometry(QtCore.QRect(70, 90, 75, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tabCalculate)
        self.label_3.setGeometry(QtCore.QRect(70, 160, 75, 20))
        self.label_3.setObjectName("label_3")
        self.comboNum1 = QtWidgets.QComboBox(self.tabCalculate)
        self.comboNum1.setGeometry(QtCore.QRect(520, 90, 161, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.comboNum1.setFont(font)
        self.comboNum1.setCurrentText("")
        self.comboNum1.setObjectName("comboNum1")
        self.comboNum2 = QtWidgets.QComboBox(self.tabCalculate)
        self.comboNum2.setGeometry(QtCore.QRect(520, 160, 161, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.comboNum2.setFont(font)
        self.comboNum2.setObjectName("comboNum2")
        self.btnAdd = QtWidgets.QPushButton(self.tabCalculate)
        self.btnAdd.setGeometry(QtCore.QRect(120, 280, 150, 30))
        self.btnAdd.setObjectName("btnAdd")
        self.btnSub = QtWidgets.QPushButton(self.tabCalculate)
        self.btnSub.setGeometry(QtCore.QRect(325, 280, 150, 30))
        self.btnSub.setObjectName("btnSub")
        self.btnMul = QtWidgets.QPushButton(self.tabCalculate)
        self.btnMul.setGeometry(QtCore.QRect(530, 280, 150, 30))
        self.btnMul.setObjectName("btnMul")
        self.btnAnd = QtWidgets.QPushButton(self.tabCalculate)
        self.btnAnd.setGeometry(QtCore.QRect(530, 330, 150, 30))
        self.btnAnd.setObjectName("btnAnd")
        self.btnOr = QtWidgets.QPushButton(self.tabCalculate)
        self.btnOr.setGeometry(QtCore.QRect(325, 330, 150, 30))
        self.btnOr.setObjectName("btnOr")
        self.btnDiv = QtWidgets.QPushButton(self.tabCalculate)
        self.btnDiv.setGeometry(QtCore.QRect(120, 330, 150, 30))
        self.btnDiv.setObjectName("btnDiv")
        self.btnXor = QtWidgets.QPushButton(self.tabCalculate)
        self.btnXor.setGeometry(QtCore.QRect(530, 380, 150, 30))
        self.btnXor.setObjectName("btnXor")
        self.btnNor = QtWidgets.QPushButton(self.tabCalculate)
        self.btnNor.setGeometry(QtCore.QRect(325, 380, 150, 30))
        self.btnNor.setObjectName("btnNor")
        self.btnNot = QtWidgets.QPushButton(self.tabCalculate)
        self.btnNot.setGeometry(QtCore.QRect(120, 380, 150, 30))
        self.btnNot.setObjectName("btnNot")
        self.txtResult = QtWidgets.QLineEdit(self.tabCalculate)
        self.txtResult.setGeometry(QtCore.QRect(150, 230, 365, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.txtResult.setFont(font)
        self.txtResult.setObjectName("txtResult")
        self.label_4 = QtWidgets.QLabel(self.tabCalculate)
        self.label_4.setGeometry(QtCore.QRect(70, 230, 75, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tabCalculate)
        self.label_5.setGeometry(QtCore.QRect(300, 20, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.comboResult = QtWidgets.QComboBox(self.tabCalculate)
        self.comboResult.setGeometry(QtCore.QRect(520, 230, 161, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.comboResult.setFont(font)
        self.comboResult.setObjectName("comboResult")
        self.btnLshift = QtWidgets.QPushButton(self.tabCalculate)
        self.btnLshift.setGeometry(QtCore.QRect(120, 430, 150, 30))
        self.btnLshift.setObjectName("btnLshift")
        self.btnRshift = QtWidgets.QPushButton(self.tabCalculate)
        self.btnRshift.setGeometry(QtCore.QRect(325, 430, 150, 30))
        self.btnRshift.setObjectName("btnRshift")
        self.btnClear1 = QtWidgets.QPushButton(self.tabCalculate)
        self.btnClear1.setGeometry(QtCore.QRect(520, 120, 161, 30))
        self.btnClear1.setObjectName("btnClear1")
        self.btnClear2 = QtWidgets.QPushButton(self.tabCalculate)
        self.btnClear2.setGeometry(QtCore.QRect(520, 190, 161, 30))
        self.btnClear2.setObjectName("btnClear2")
        self.tabWidget.addTab(self.tabCalculate, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 5, 600, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

###########################################################################
# APP EVENT LISTENERS
###########################################################################
        # Initialize the app
        self.init()
        # Button "Convert" clicked
        self.btnConvert.clicked.connect(self.btnConvertClicked)
        # ComboBox Number base changed
        self.comboNum.currentIndexChanged.connect(self.comboNumChanged)
        # ComboBox Number 1 base changed
        self.comboNum1.currentIndexChanged.connect(self.comboNum1Changed)
        # ComboBox Number 2 base changed
        self.comboNum2.currentIndexChanged.connect(self.comboNum2Changed)
        # ComboBox Result base changed
        self.comboResult.currentIndexChanged.connect(
            self.comboResultChanged)
        # Button "ADD" clicked
        self.btnAdd.clicked.connect(self.btnAddClicked)
        # Button "SUBTRACT" clicked
        self.btnSub.clicked.connect(self.btnSubClicked)
        # Button "MULTIPLY" clicked
        self.btnMul.clicked.connect(self.btnMulClicked)
        # Button "DIVIDE" clicked
        self.btnDiv.clicked.connect(self.btnDivClicked)
        # Button "AND" clicked
        self.btnAnd.clicked.connect(self.btnAndClicked)
        # Button "OR" clicked
        self.btnOr.clicked.connect(self.btnOrClicked)
        # Button "XOR" clicked
        self.btnXor.clicked.connect(self.btnXorClicked)
        # Button "NOR" clicked
        self.btnNor.clicked.connect(self.btnNorClicked)
        # Button "NOT" clicked
        self.btnNot.clicked.connect(self.btnNotClicked)
        # Button "LSHIFT" clicked
        self.btnLshift.clicked.connect(self.btnLshiftClicked)
        # Button "RSHIFT" clicked
        self.btnRshift.clicked.connect(self.btnRshiftClicked)

###########################################################################
# APP RETRANSLATION (GUI CODE GENERATED)
###########################################################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Team Speak"))
        self.label_6.setText(_translate("MainWindow", "CONVERTER"))
        self.label_7.setText(_translate("MainWindow", "Decimal:"))
        self.label_8.setText(_translate("MainWindow", "Binary:"))
        self.label_9.setText(_translate("MainWindow", "SEM:"))
        self.label_10.setText(_translate("MainWindow", "Hex:"))
        self.btnConvert.setText(_translate("MainWindow", "CONVERT"))
        self.txtError.setText(_translate("MainWindow", "Error Messages!"))
        self.label_12.setText(_translate("MainWindow", "Number:"))
        self.label_13.setText(_translate("MainWindow", "Format:"))
        self.label_11.setText(_translate("MainWindow", "Sign"))
        self.label_14.setText(_translate("MainWindow", "Exponent"))
        self.label_15.setText(_translate("MainWindow", "Mantissa"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabConvert), _translate("MainWindow", "Converter"))
        self.label_2.setText(_translate("MainWindow", "Number 1:"))
        self.label_3.setText(_translate("MainWindow", "Number 2:"))
        self.btnAdd.setText(_translate("MainWindow", "ADD"))
        self.btnSub.setText(_translate("MainWindow", "SUBTRACT"))
        self.btnMul.setText(_translate("MainWindow", "MULTIPLY"))
        self.btnAnd.setText(_translate("MainWindow", "AND"))
        self.btnOr.setText(_translate("MainWindow", "OR"))
        self.btnDiv.setText(_translate("MainWindow", "DIVIDE"))
        self.btnXor.setText(_translate("MainWindow", "XOR"))
        self.btnNor.setText(_translate("MainWindow", "NOR"))
        self.btnNot.setText(_translate("MainWindow", "NOT"))
        self.label_4.setText(_translate("MainWindow", "Result:"))
        self.label_5.setText(_translate("MainWindow", "CALCULATOR"))
        self.btnLshift.setText(_translate("MainWindow", "LSHIFT"))
        self.btnRshift.setText(_translate("MainWindow", "RSHIFT"))
        self.btnClear1.setText(_translate("MainWindow", "CLEAR"))
        self.btnClear2.setText(_translate("MainWindow", "CLEAR"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCalculate), _translate("MainWindow", "Calculator"))
        self.label.setText(_translate("MainWindow", "Number Converter and Calculator"))

###########################################################################
# MAIN FUCNTION (APP START FROM HERE)
###########################################################################
# Main Function
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

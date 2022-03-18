from ast import Num
from glob import glob
from PyQt5 import QtCore, QtGui, QtWidgets
from number import Number

# Global variables
options = {
    0: 'Decimal',
    1: 'Binary',
    2: 'Hex',
    3: 'SEM',
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
    # APP EVENT FUNCTIONS
    ###########################################################################
    # App initialization
    def init(self):
        print('App initializing...')
        self.comboNum1.addItems(options.values())
        self.comboNum2.addItems(options.values())
        self.comboResult.addItems(options.values())
        self.comboNum.addItems(options.values())
        print('App initialized!')

    # ComboBox 'Number' changed
    def comboNumChanged(self):
        global optionNum
        optionNum = self.comboNum.currentIndex()

    # Button 'Convert' clicked
    def btnConvertClicked(self):
        global num
        try:
            if optionNum == 0:
                print("Decimal chosen")
                num.set_from_float(float(self.txtNum.text()))
                self.txtBinary.setText(str(num.get_binary()))
                self.txtHex.setText(str(num.get_hex()))
                self.txtSem.setText(str(num.get_sem()))
                self.txtDecimal.setText(str(num.get_float()))
            elif optionNum == 1:
                print("Binary chosen")
                num.set_from_binary(self.txtNum.text())
                self.txtBinary.setText(str(num.get_binary()))
                self.txtHex.setText(str(num.get_hex()))
                self.txtSem.setText(str(num.get_sem()))
                self.txtDecimal.setText(str(num.get_float()))
            elif optionNum == 2:
                print("Hex chosen")
                num.set_from_hex(self.txtNum.text())
                self.txtBinary.setText(str(num.get_binary()))
                self.txtHex.setText(str(num.get_hex()))
                self.txtSem.setText(str(num.get_sem()))
                self.txtDecimal.setText(str(num.get_float()))
            elif optionNum == 3:
                print("SEM chosen")
                num.set_from_sem(self.txtNum.text())
                self.txtBinary.setText(str(num.get_binary()))
                self.txtHex.setText(str(num.get_hex()))
                self.txtSem.setText(str(num.get_sem()))
                self.txtDecimal.setText(str(num.get_float()))
        except:
            self.txtDecimal.setText('Error! Please enter a valid number.')
            self.txtBinary.setText('Error! Please enter a valid number.')
            self.txtHex.setText('Error! Please enter a valid number.')
            self.txtSem.setText('Error! Please enter a valid number.')

    # ComboBox 'Number 1' changed
    def comboNum1Changed(self):
        global optionNum1
        optionNum1 = self.comboNum1.currentIndex()

    # ComboBox 'Number 2' changed
    def comboNum2Changed(self):
        global optionNum2
        optionNum2 = self.comboNum2.currentIndex()

    # ComboBox 'Result' changed
    def comboResultChanged(self):
        global optionResult
        optionResult = self.comboResult.currentIndex()
    ###########################################################################

    # GENERATED GUI CODES
    ###########################################################################
    def setupUi(self, MainWindow):
        MainWindow.setObjectName('MainWindow')
        MainWindow.resize(800, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(5, 125, 790, 551))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName('tabWidget')
        self.tabConvert = QtWidgets.QWidget()
        self.tabConvert.setObjectName('tabConvert')
        self.label_6 = QtWidgets.QLabel(self.tabConvert)
        self.label_6.setGeometry(QtCore.QRect(325, 20, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName('label_6')
        self.txtNum = QtWidgets.QLineEdit(self.tabConvert)
        self.txtNum.setGeometry(QtCore.QRect(110, 100, 365, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.txtNum.setFont(font)
        self.txtNum.setObjectName('txtNum')
        self.comboNum = QtWidgets.QComboBox(self.tabConvert)
        self.comboNum.setGeometry(QtCore.QRect(490, 100, 161, 22))
        self.comboNum.setObjectName('comboNum')
        self.txtDecimal = QtWidgets.QLineEdit(self.tabConvert)
        self.txtDecimal.setEnabled(False)
        self.txtDecimal.setGeometry(QtCore.QRect(280, 180, 365, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.txtDecimal.setFont(font)
        self.txtDecimal.setObjectName('txtDecimal')
        self.txtBinary = QtWidgets.QLineEdit(self.tabConvert)
        self.txtBinary.setEnabled(False)
        self.txtBinary.setGeometry(QtCore.QRect(280, 250, 365, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.txtBinary.setFont(font)
        self.txtBinary.setObjectName('txtBinary')
        self.txtSem = QtWidgets.QLineEdit(self.tabConvert)
        self.txtSem.setEnabled(False)
        self.txtSem.setGeometry(QtCore.QRect(280, 320, 365, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.txtSem.setFont(font)
        self.txtSem.setObjectName('txtSem')
        self.txtHex = QtWidgets.QLineEdit(self.tabConvert)
        self.txtHex.setEnabled(False)
        self.txtHex.setGeometry(QtCore.QRect(280, 390, 365, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.txtHex.setFont(font)
        self.txtHex.setObjectName('txtHex')
        self.label_7 = QtWidgets.QLabel(self.tabConvert)
        self.label_7.setGeometry(QtCore.QRect(210, 180, 60, 20))
        self.label_7.setObjectName('label_7')
        self.label_8 = QtWidgets.QLabel(self.tabConvert)
        self.label_8.setGeometry(QtCore.QRect(210, 250, 60, 20))
        self.label_8.setObjectName('label_8')
        self.label_9 = QtWidgets.QLabel(self.tabConvert)
        self.label_9.setGeometry(QtCore.QRect(210, 320, 60, 20))
        self.label_9.setObjectName('label_9')
        self.label_10 = QtWidgets.QLabel(self.tabConvert)
        self.label_10.setGeometry(QtCore.QRect(210, 390, 60, 20))
        self.label_10.setObjectName('label_10')
        self.btnConvert = QtWidgets.QPushButton(self.tabConvert)
        self.btnConvert.setGeometry(QtCore.QRect(325, 460, 150, 30))
        self.btnConvert.setObjectName('btnConvert')
        self.tabWidget.addTab(self.tabConvert, '')
        self.tabCalculate = QtWidgets.QWidget()
        self.tabCalculate.setObjectName('tabCalculate')
        self.txtNum1 = QtWidgets.QLineEdit(self.tabCalculate)
        self.txtNum1.setGeometry(QtCore.QRect(150, 90, 365, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.txtNum1.setFont(font)
        self.txtNum1.setObjectName('txtNum1')
        self.txtNum2 = QtWidgets.QLineEdit(self.tabCalculate)
        self.txtNum2.setGeometry(QtCore.QRect(150, 160, 365, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.txtNum2.setFont(font)
        self.txtNum2.setObjectName('txtNum2')
        self.label_2 = QtWidgets.QLabel(self.tabCalculate)
        self.label_2.setGeometry(QtCore.QRect(80, 90, 60, 20))
        self.label_2.setObjectName('label_2')
        self.label_3 = QtWidgets.QLabel(self.tabCalculate)
        self.label_3.setGeometry(QtCore.QRect(80, 160, 60, 20))
        self.label_3.setObjectName('label_3')
        self.comboNum1 = QtWidgets.QComboBox(self.tabCalculate)
        self.comboNum1.setGeometry(QtCore.QRect(520, 90, 161, 22))
        self.comboNum1.setObjectName('comboNum1')
        self.comboNum2 = QtWidgets.QComboBox(self.tabCalculate)
        self.comboNum2.setGeometry(QtCore.QRect(520, 160, 161, 22))
        self.comboNum2.setObjectName('comboNum2')
        self.btnAdd = QtWidgets.QPushButton(self.tabCalculate)
        self.btnAdd.setGeometry(QtCore.QRect(120, 310, 150, 30))
        self.btnAdd.setObjectName('btnAdd')
        self.btnSub = QtWidgets.QPushButton(self.tabCalculate)
        self.btnSub.setGeometry(QtCore.QRect(325, 310, 150, 30))
        self.btnSub.setObjectName('btnSub')
        self.btnMul = QtWidgets.QPushButton(self.tabCalculate)
        self.btnMul.setGeometry(QtCore.QRect(530, 310, 150, 30))
        self.btnMul.setObjectName('btnMul')
        self.btnAnd = QtWidgets.QPushButton(self.tabCalculate)
        self.btnAnd.setGeometry(QtCore.QRect(530, 360, 150, 30))
        self.btnAnd.setObjectName('btnAnd')
        self.btnOr = QtWidgets.QPushButton(self.tabCalculate)
        self.btnOr.setGeometry(QtCore.QRect(325, 360, 150, 30))
        self.btnOr.setObjectName('btnOr')
        self.btnDiv = QtWidgets.QPushButton(self.tabCalculate)
        self.btnDiv.setGeometry(QtCore.QRect(120, 360, 150, 30))
        self.btnDiv.setObjectName('btnDiv')
        self.btnXor = QtWidgets.QPushButton(self.tabCalculate)
        self.btnXor.setGeometry(QtCore.QRect(530, 410, 150, 30))
        self.btnXor.setObjectName('btnXor')
        self.btnNor = QtWidgets.QPushButton(self.tabCalculate)
        self.btnNor.setGeometry(QtCore.QRect(325, 410, 150, 30))
        self.btnNor.setObjectName('btnNor')
        self.btnNot = QtWidgets.QPushButton(self.tabCalculate)
        self.btnNot.setGeometry(QtCore.QRect(120, 410, 150, 30))
        self.btnNot.setObjectName('btnNot')
        self.txtResult = QtWidgets.QLineEdit(self.tabCalculate)
        self.txtResult.setEnabled(False)
        self.txtResult.setGeometry(QtCore.QRect(150, 230, 365, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.txtResult.setFont(font)
        self.txtResult.setObjectName('txtResult')
        self.label_4 = QtWidgets.QLabel(self.tabCalculate)
        self.label_4.setGeometry(QtCore.QRect(99, 230, 41, 20))
        self.label_4.setObjectName('label_4')
        self.label_5 = QtWidgets.QLabel(self.tabCalculate)
        self.label_5.setGeometry(QtCore.QRect(325, 20, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName('label_5')
        self.comboResult = QtWidgets.QComboBox(self.tabCalculate)
        self.comboResult.setGeometry(QtCore.QRect(520, 230, 161, 22))
        self.comboResult.setObjectName('comboResult')
        self.label_11 = QtWidgets.QLabel(self.tabCalculate)
        self.label_11.setGeometry(QtCore.QRect(100, 480, 600, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName('label_11')
        self.tabWidget.addTab(self.tabCalculate, '')
        self.tabAbout = QtWidgets.QWidget()
        self.tabAbout.setObjectName('tabAbout')
        self.tabWidget.addTab(self.tabAbout, '')
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 5, 600, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName('label')
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # APP EVENT LISTENERS
        ###########################################################################
        self.init()

        self.btnConvert.clicked.connect(self.btnConvertClicked)
        self.comboNum.currentIndexChanged.connect(self.comboNumChanged)

        self.comboNum1.currentIndexChanged.connect(self.comboNum1Changed)
        self.comboNum2.currentIndexChanged.connect(self.comboNum2Changed)
        self.comboResult.currentIndexChanged.connect(self.comboResultChanged)
        ###########################################################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate('MainWindow', 'Team Speak'))
        self.label_6.setText(_translate('MainWindow', 'Converter'))
        self.label_7.setText(_translate('MainWindow', 'Decimal:'))
        self.label_8.setText(_translate('MainWindow', 'Binary:'))
        self.label_9.setText(_translate('MainWindow', 'SEM:'))
        self.label_10.setText(_translate('MainWindow', 'Hex:'))
        self.btnConvert.setText(_translate('MainWindow', 'CONVERT'))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tabConvert), _translate('MainWindow', 'Converter'))
        self.label_2.setText(_translate('MainWindow', 'Number 1:'))
        self.label_3.setText(_translate('MainWindow', 'Number 2:'))
        self.btnAdd.setText(_translate('MainWindow', 'ADD'))
        self.btnSub.setText(_translate('MainWindow', 'SUBTRACT'))
        self.btnMul.setText(_translate('MainWindow', 'MULTIPLY'))
        self.btnAnd.setText(_translate('MainWindow', 'AND'))
        self.btnOr.setText(_translate('MainWindow', 'OR'))
        self.btnDiv.setText(_translate('MainWindow', 'DIVIDE'))
        self.btnXor.setText(_translate('MainWindow', 'XOR'))
        self.btnNor.setText(_translate('MainWindow', 'NOR'))
        self.btnNot.setText(_translate('MainWindow', 'NOT'))
        self.label_4.setText(_translate('MainWindow', 'Result:'))
        self.label_5.setText(_translate('MainWindow', 'Calculator'))
        self.label_11.setText(_translate(
            'MainWindow', '(OR, AND, NOT, NOR, XOR, LSHIFT, RSHIFT only support decimal numbers)'))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tabCalculate), _translate('MainWindow', 'Calculator'))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tabAbout), _translate('MainWindow', 'About'))
        self.label.setText(_translate(
            'MainWindow', 'Number Converter and Calculator'))
    ###########################################################################


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

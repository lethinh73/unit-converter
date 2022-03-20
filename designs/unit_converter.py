# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'unit_converter.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 680)
        MainWindow.setMaximumSize(QtCore.QSize(800, 680))
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
        self.label_6.setGeometry(QtCore.QRect(325, 20, 150, 50))
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
        self.comboNum.setGeometry(QtCore.QRect(490, 100, 161, 22))
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
        self.txtSem = QtWidgets.QLineEdit(self.tabConvert)
        self.txtSem.setGeometry(QtCore.QRect(280, 320, 365, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.txtSem.setFont(font)
        self.txtSem.setObjectName("txtSem")
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
        self.label_12.setGeometry(QtCore.QRect(110, 70, 60, 20))
        self.label_12.setObjectName("label_12")
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
        self.label_2.setGeometry(QtCore.QRect(80, 90, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tabCalculate)
        self.label_3.setGeometry(QtCore.QRect(80, 160, 60, 20))
        self.label_3.setObjectName("label_3")
        self.comboNum1 = QtWidgets.QComboBox(self.tabCalculate)
        self.comboNum1.setGeometry(QtCore.QRect(520, 90, 161, 22))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.comboNum1.setFont(font)
        self.comboNum1.setCurrentText("")
        self.comboNum1.setObjectName("comboNum1")
        self.comboNum2 = QtWidgets.QComboBox(self.tabCalculate)
        self.comboNum2.setGeometry(QtCore.QRect(520, 160, 161, 22))
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
        self.label_4.setGeometry(QtCore.QRect(99, 230, 41, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tabCalculate)
        self.label_5.setGeometry(QtCore.QRect(325, 20, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.comboResult = QtWidgets.QComboBox(self.tabCalculate)
        self.comboResult.setGeometry(QtCore.QRect(520, 230, 161, 22))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.comboResult.setFont(font)
        self.comboResult.setObjectName("comboResult")
        self.label_11 = QtWidgets.QLabel(self.tabCalculate)
        self.label_11.setGeometry(QtCore.QRect(100, 480, 600, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.btnLshift = QtWidgets.QPushButton(self.tabCalculate)
        self.btnLshift.setGeometry(QtCore.QRect(220, 430, 150, 30))
        self.btnLshift.setObjectName("btnLshift")
        self.btnRshift = QtWidgets.QPushButton(self.tabCalculate)
        self.btnRshift.setGeometry(QtCore.QRect(430, 430, 150, 30))
        self.btnRshift.setObjectName("btnRshift")
        self.tabWidget.addTab(self.tabCalculate, "")
        self.tabAbout = QtWidgets.QWidget()
        self.tabAbout.setObjectName("tabAbout")
        self.tabWidget.addTab(self.tabAbout, "")
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Team Speak"))
        self.label_6.setText(_translate("MainWindow", "CONVERTER"))
        self.label_7.setText(_translate("MainWindow", "Decimal:"))
        self.label_8.setText(_translate("MainWindow", "Binary:"))
        self.label_9.setText(_translate("MainWindow", "SEM:"))
        self.label_10.setText(_translate("MainWindow", "Hex:"))
        self.btnConvert.setText(_translate("MainWindow", "CONVERT"))
        self.txtError.setText(_translate("MainWindow", "TextLabel"))
        self.label_12.setText(_translate("MainWindow", "Number:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tabConvert), _translate("MainWindow", "Converter"))
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
        self.label_11.setText(_translate(
            "MainWindow", "(OR, AND, NOT, NOR, XOR, LSHIFT, RSHIFT don\'t support floating-point decimals)"))
        self.btnLshift.setText(_translate("MainWindow", "LSHIFT"))
        self.btnRshift.setText(_translate("MainWindow", "RSHIFT"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tabCalculate), _translate("MainWindow", "Calculator"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tabAbout), _translate("MainWindow", "About"))
        self.label.setText(_translate(
            "MainWindow", "Number Converter and Calculator"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

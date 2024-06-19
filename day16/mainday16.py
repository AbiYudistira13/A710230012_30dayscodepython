from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 400)

        # Main title label
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 50, 300, 50))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        # Price label and line edit
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 120, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(200, 120, 300, 30))
        self.lineEdit.setObjectName("lineEdit")

        # Tax label and combo box
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(100, 170, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(200, 170, 300, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("5%")
        self.comboBox.addItem("10%")
        self.comboBox.addItem("15%")

        # Calculate button
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(200, 220, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        # Result label
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 270, 400, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Connect the button click to the function
        self.pushButton.clicked.connect(self.calculate_tax)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Perhitungan Pajak"))
        self.label.setText(_translate("Dialog", "PERHITUNGAN PAJAK"))
        self.label_2.setText(_translate("Dialog", "Harga:"))
        self.label_4.setText(_translate("Dialog", "Pajak:"))
        self.pushButton.setText(_translate("Dialog", "Hitung Pajak"))
        self.label_3.setText(_translate("Dialog", "Total Harga Beserta Pajak Adalah:"))

    def calculate_tax(self):
        try:
            price = float(self.lineEdit.text())
            tax_rate_str = self.comboBox.currentText()
            tax_rate = float(tax_rate_str.strip('%')) / 100
            total_price = price + (price * tax_rate)
            self.label_3.setText(f"Total Harga Beserta Pajak Adalah: Rp {total_price:.2f}")
        except ValueError:
            self.label_3.setText("Input harga tidak valid. Masukkan angka yang benar.")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

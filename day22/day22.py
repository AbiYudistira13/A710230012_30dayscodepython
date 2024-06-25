from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tablePlayers = QtWidgets.QTableWidget(self.centralwidget)
        self.tablePlayers.setGeometry(QtCore.QRect(10, 10, 580, 192))
        self.tablePlayers.setObjectName("tablePlayers")
        self.tablePlayers.setColumnCount(0)
        self.tablePlayers.setRowCount(0)
        self.inputName = QtWidgets.QLineEdit(self.centralwidget)
        self.inputName.setGeometry(QtCore.QRect(10, 210, 113, 20))
        self.inputName.setObjectName("inputName")
        self.inputNumber = QtWidgets.QLineEdit(self.centralwidget)
        self.inputNumber.setGeometry(QtCore.QRect(130, 210, 113, 20))
        self.inputNumber.setObjectName("inputNumber")
        self.inputPosition = QtWidgets.QLineEdit(self.centralwidget)
        self.inputPosition.setGeometry(QtCore.QRect(250, 210, 113, 20))
        self.inputPosition.setObjectName("inputPosition")
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setGeometry(QtCore.QRect(370, 210, 75, 23))
        self.btnAdd.setObjectName("btnAdd")
        self.btnDelete = QtWidgets.QPushButton(self.centralwidget)
        self.btnDelete.setGeometry(QtCore.QRect(450, 210, 75, 23))
        self.btnDelete.setObjectName("btnDelete")
        self.btnUpdate = QtWidgets.QPushButton(self.centralwidget)
        self.btnUpdate.setGeometry(QtCore.QRect(530, 210, 75, 23))
        self.btnUpdate.setObjectName("btnUpdate")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Data Pemain Voli"))
        self.inputName.setPlaceholderText(_translate("MainWindow", "Nama"))
        self.inputNumber.setPlaceholderText(_translate("MainWindow", "Nomor Punggung"))
        self.inputPosition.setPlaceholderText(_translate("MainWindow", "Posisi"))
        self.btnAdd.setText(_translate("MainWindow", "Tambah"))
        self.btnDelete.setText(_translate("MainWindow", "Hapus"))
        self.btnUpdate.setText(_translate("MainWindow", "Perbarui"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

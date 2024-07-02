from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 10, 100, 20))
        self.label.setObjectName("label")
        self.label_pickup = QtWidgets.QLabel(self.centralwidget)
        self.label_pickup.setGeometry(QtCore.QRect(50, 50, 120, 20))
        self.label_pickup.setObjectName("label_pickup")
        self.lineEdit_pickup = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pickup.setGeometry(QtCore.QRect(180, 50, 160, 20))
        self.lineEdit_pickup.setObjectName("lineEdit_pickup")
        self.label_destination = QtWidgets.QLabel(self.centralwidget)
        self.label_destination.setGeometry(QtCore.QRect(50, 90, 120, 20))
        self.label_destination.setObjectName("label_destination")
        self.lineEdit_destination = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_destination.setGeometry(QtCore.QRect(180, 90, 160, 20))
        self.lineEdit_destination.setObjectName("lineEdit_destination")
        self.label_vehicle = QtWidgets.QLabel(self.centralwidget)
        self.label_vehicle.setGeometry(QtCore.QRect(50, 130, 120, 20))
        self.label_vehicle.setObjectName("label_vehicle")
        self.comboBox_vehicle = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_vehicle.setGeometry(QtCore.QRect(180, 130, 160, 20))
        self.comboBox_vehicle.setObjectName("comboBox_vehicle")
        self.comboBox_vehicle.addItem("")
        self.comboBox_vehicle.addItem("")
        self.comboBox_vehicle.addItem("")
        self.pushButton_order = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_order.setGeometry(QtCore.QRect(150, 180, 100, 30))
        self.pushButton_order.setObjectName("pushButton_order")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Aplikasi Ojek Online"))
        self.label.setText(_translate("MainWindow", "Ojek Online"))
        self.label_pickup.setText(_translate("MainWindow", "Lokasi Penjemputan:"))
        self.label_destination.setText(_translate("MainWindow", "Lokasi Tujuan:"))
        self.label_vehicle.setText(_translate("MainWindow", "Jenis Kendaraan:"))
        self.comboBox_vehicle.setItemText(0, _translate("MainWindow", "Motor"))
        self.comboBox_vehicle.setItemText(1, _translate("MainWindow", "Mobil"))
        self.comboBox_vehicle.setItemText(2, _translate("MainWindow", "Bajaj"))
        self.pushButton_order.setText(_translate("MainWindow", "Pesan"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

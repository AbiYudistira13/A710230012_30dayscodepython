import sys
import os
from PyQt5 import QtWidgets
from day29 import Ui_MainWindow

class OjekOnlineApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(OjekOnlineApp, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_order.clicked.connect(self.order_ojek)
        self.orders_folder = 'orders'

        # Membuat folder orders jika belum ada
        if not os.path.exists(self.orders_folder):
            os.makedirs(self.orders_folder)

    def order_ojek(self):
        pickup = self.lineEdit_pickup.text()
        destination = self.lineEdit_destination.text()
        vehicle = self.comboBox_vehicle.currentText()
        message = f"Anda telah memesan {vehicle} dari {pickup} ke {destination}."
        QtWidgets.QMessageBox.information(self, "Pesanan Dikonfirmasi", message)
        self.save_order(pickup, destination, vehicle)

    def save_order(self, pickup, destination, vehicle):
        # Menyimpan data ke dalam file teks di folder orders
        with open(os.path.join(self.orders_folder, 'orders.txt'), 'a') as file:
            file.write(f"Pickup: {pickup}, Destination: {destination}, Vehicle: {vehicle}\n")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = OjekOnlineApp()
    mainWin.show()
    sys.exit(app.exec_())
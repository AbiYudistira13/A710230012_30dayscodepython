import sys
from PyQt5 import QtWidgets
from day26 import Ui_MainWindow  # Import hasil konversi dari PyQt Designer

class MotorBeliApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Data motor (bisa disesuaikan)
        self.motor_data = {
            'Honda': {'Vario': 18000000, 'Beat': 15000000},
            'Yamaha': {'NMax': 25000000, 'Mio': 14000000}
        }
        
        # Isi ComboBox merek motor
        self.comboBox_brand.addItems(self.motor_data.keys())
        
        # Event handlers
        self.comboBox_brand.currentTextChanged.connect(self.update_models)
        self.comboBox_model.currentTextChanged.connect(self.update_price)
        self.pushButton_buy.clicked.connect(self.buy_motor)
        
    def update_models(self, brand):
        self.comboBox_model.clear()
        if brand in self.motor_data:
            self.comboBox_model.addItems(self.motor_data[brand].keys())
        
    def update_price(self, model):
        brand = self.comboBox_brand.currentText()
        if brand in self.motor_data and model in self.motor_data[brand]:
            self.lineEdit_price.setText(str(self.motor_data[brand][model]))
        else:
            self.lineEdit_price.setText('')
    
    def buy_motor(self):
        brand = self.comboBox_brand.currentText()
        model = self.comboBox_model.currentText()
        price = self.lineEdit_price.text()
        quantity = self.spinBox_quantity.value()
        
        if not brand or not model or not price:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Harap pilih merek dan model motor yang valid.')
            return
        
        total_price = int(price) * quantity
        message = f'Anda telah membeli {quantity} {model} {brand} dengan total harga Rp {total_price}.'
        QtWidgets.QMessageBox.information(self, 'Pembelian Berhasil', message)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MotorBeliApp()
    window.show()
    sys.exit(app.exec_())
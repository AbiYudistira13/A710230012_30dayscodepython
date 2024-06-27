import sys
from PyQt5 import QtWidgets, uic

class KasirApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(KasirApp, self).__init__()
        uic.loadUi('day24.ui', self)

        # Menemukan widget
        self.lineEditNamaBarang = self.findChild(QtWidgets.QLineEdit, 'lineEditNamaBarang')
        self.lineEditHarga = self.findChild(QtWidgets.QLineEdit, 'lineEditHarga')
        self.lineEditJumlah = self.findChild(QtWidgets.QLineEdit, 'lineEditJumlah')
        self.pushButtonTambah = self.findChild(QtWidgets.QPushButton, 'pushButtonTambah')
        self.tableWidget = self.findChild(QtWidgets.QTableWidget, 'tableWidget')
        self.pushButtonTotal = self.findChild(QtWidgets.QPushButton, 'pushButtonTotal')
        self.labelTotal = self.findChild(QtWidgets.QLabel, 'labelTotal')

        # Menghubungkan tombol dengan fungsi
        self.pushButtonTambah.clicked.connect(self.tambah_barang)
        self.pushButtonTotal.clicked.connect(self.hitung_total)

        self.show()

    def tambah_barang(self):
        nama_barang = self.lineEditNamaBarang.text()
        harga = float(self.lineEditHarga.text())
        jumlah = int(self.lineEditJumlah.text())
        total = harga * jumlah

        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)

        self.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(nama_barang))
        self.tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(str(harga)))
        self.tableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(str(jumlah)))
        self.tableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(str(total)))

    def hitung_total(self):
        total_semua = 0
        for row in range(self.tableWidget.rowCount()):
            total_semua += float(self.tableWidget.item(row, 3).text())

        self.labelTotal.setText(f'Total: {total_semua}')

app = QtWidgets.QApplication(sys.argv)
window = KasirApp()
app.exec_()
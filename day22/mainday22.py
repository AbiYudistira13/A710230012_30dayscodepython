import sys
from PyQt5 import QtWidgets, uic

class DataPemainVoli(QtWidgets.QMainWindow):
    def __init__(self):
        super(DataPemainVoli, self).__init__()
        uic.loadUi('data_pemain_voli.ui', self)
        
        # Inisialisasi tabel
        self.tablePlayers.setColumnCount(3)
        self.tablePlayers.setHorizontalHeaderLabels(["Nama", "Nomor Punggung", "Posisi"])
        
        # Event handlers
        self.btnAdd.clicked.connect(self.add_player)
        self.btnDelete.clicked.connect(self.delete_player)
        self.btnUpdate.clicked.connect(self.update_player)
    
    def add_player(self):
        name = self.inputName.text()
        number = self.inputNumber.text()
        position = self.inputPosition.text()
        
        rowPosition = self.tablePlayers.rowCount()
        self.tablePlayers.insertRow(rowPosition)
        self.tablePlayers.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(name))
        self.tablePlayers.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(number))
        self.tablePlayers.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(position))
        
        self.clear_inputs()
    
    def delete_player(self):
        selectedRow = self.tablePlayers.currentRow()
        if selectedRow >= 0:
            self.tablePlayers.removeRow(selectedRow)
    
    def update_player(self):
        selectedRow = self.tablePlayers.currentRow()
        if selectedRow >= 0:
            name = self.inputName.text()
            number = self.inputNumber.text()
            position = self.inputPosition.text()
            
            self.tablePlayers.setItem(selectedRow, 0, QtWidgets.QTableWidgetItem(name))
            self.tablePlayers.setItem(selectedRow, 1, QtWidgets.QTableWidgetItem(number))
            self.tablePlayers.setItem(selectedRow, 2, QtWidgets.QTableWidgetItem(position))
            
            self.clear_inputs()
    
    def clear_inputs(self):
        self.inputName.clear()
        self.inputNumber.clear()
        self.inputPosition.clear()

app = QtWidgets.QApplication(sys.argv)
window = DataPemainVoli()
window.show()
app.exec_()

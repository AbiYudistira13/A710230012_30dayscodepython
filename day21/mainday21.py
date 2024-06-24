import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from day21 import Ui_MainWindow

class TutorialMasak(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(TutorialMasak, self).__init__()
        self.setupUi(self)
        
        # Contoh resep dan instruksi memasak
        self.resep = {
            "Nasi Goreng": "1. Panaskan minyak.\n2. Tumis bawang putih.\n3. Masukkan nasi.\n4. Tambahkan kecap.",
            "Ayam Goreng": "1. Lumuri ayam dengan bumbu.\n2. Panaskan minyak.\n3. Goreng ayam hingga matang."
        }
        
        # Sambungkan sinyal tombol dengan fungsi
        self.pushButton_start.clicked.connect(self.start_tutorial)
        self.pushButton_stop.clicked.connect(self.stop_tutorial)
    
    def start_tutorial(self):
        # Tampilkan resep dan instruksi memasak
        self.label_title.setText("Resep: Nasi Goreng")
        self.textEdit_instructions.setText(self.resep["Nasi Goreng"])
    
    def stop_tutorial(self):
        # Kosongkan label dan text edit
        self.label_title.setText("")
        self.textEdit_instructions.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TutorialMasak()
    window.show()
    sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from day28 import Ui_MainWindow  # Import generated UI code

class QueueApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.queue_number = 0
        
        self.btn_take_number.clicked.connect(self.take_number)
    
    def take_number(self):
        self.queue_number += 1
        self.lbl_queue_number.setText(f"Nomor Antrian: {self.queue_number}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QueueApp()
    window.show()
    sys.exit(app.exec_())

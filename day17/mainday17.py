from PyQt5.QtWidgets import QApplication, QMainWindow
from day17 import Ui_Form

class HelloWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(HelloWindow, self).__init__(parent)
        self.setupUi(self)

app = QApplication([])
window = HelloWindow()
window.show()
app.exec_()
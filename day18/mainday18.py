from PyQt5.QtWidgets import QApplication, QDialog
from day18 import Ui_Dialog

class DialogWindow(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(DialogWindow, self).__init__(parent)
        self.setupUi(self)

app = QApplication([])
window = DialogWindow()
window.show()
app.exec_()
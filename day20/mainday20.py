import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QInputDialog
from day20 import Ui_MainWindow

class FootballPlayersApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Data pemain (contoh)
        self.players = [
            {"name": "Lionel Messi", "position": "Forward", "number": 10},
            {"name": "Cristiano Ronaldo", "position": "Forward", "number": 7},
            {"name": "Neymar Jr", "position": "Forward", "number": 10},
        ]
        
        self.load_data()
        
        # Menghubungkan tombol
        self.ui.addButton.clicked.connect(self.add_player)
        self.ui.removeButton.clicked.connect(self.remove_player)

    def load_data(self):
        self.ui.tableWidget.setRowCount(len(self.players))
        for row, player in enumerate(self.players):
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(player["name"]))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(player["position"]))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(player["number"])))

    def add_player(self):
        name, ok = QInputDialog.getText(self, "Input Dialog", "Enter player name:")
        if ok:
            position, ok = QInputDialog.getText(self, "Input Dialog", "Enter player position:")
            if ok:
                number, ok = QInputDialog.getInt(self, "Input Dialog", "Enter player number:")
                if ok:
                    new_player = {"name": name, "position": position, "number": number}
                    self.players.append(new_player)
                    self.load_data()

    def remove_player(self):
        current_row = self.ui.tableWidget.currentRow()
        if current_row >= 0:
            del self.players[current_row]
            self.load_data()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FootballPlayersApp()
    window.show()
    sys.exit(app.exec_())
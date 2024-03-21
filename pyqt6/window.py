import sys

from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(200, 100, 400, 300)
        self.setWindowTitle("PyQt")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

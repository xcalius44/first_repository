import sys

from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setMinimumSize(450, 350)
        self.setWindowTitle("MainWindow")
        self.setUpMainWindow()
        self.createActions()
        self.createMenu()
        self.show()

    def setUpMainWindow(self):
        pass

    def createActions(self):
        self.quit_act = QAction("&Вихід")
        self.quit_act.setShortcut("Ctrl+Q")
        self.quit_act.triggered.connect(self.close)

    def createMenu(self):
        self.menuBar().setNativeMenuBar(False)

        file_menu = self.menuBar().addMenu("&Файл")
        file_menu.addAction(self.quit_act)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QMessageBox,
    QTextEdit,
    QFileDialog,
    QInputDialog,
    QFontDialog,
    QColorDialog,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon, QTextCursor, QColor


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setMinimumSize(400, 500)
        self.setWindowTitle("PyQt Notepad")
        self.setUpMainWindow()
        self.createActions()
        self.createMenu()
        self.show()

    def setUpMainWindow(self):
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

    def createActions(self):
        self.quit_act = QAction(QIcon("images/exit.png"), "&Вихід")
        self.quit_act.setShortcut("Ctrl+Q")
        self.quit_act.triggered.connect(self.close)

        self.new_act = QAction(QIcon("images/new_file.png"), "Новий")
        self.new_act.setShortcut("Ctrl+N")
        # self.new_act.triggered.connect(self.clearText)

        self.open_act = QAction(QIcon("images/open_file.png"), "Відкрити")
        self.open_act.setShortcut("Ctrl+O")
        # self.open_act.triggered.connect(self.openFile)

        self.save_act = QAction(QIcon("images/save_file.png"), "Зберегти")
        self.save_act.setShortcut("Ctrl+S")
        # self.save_act.triggered.connect(self.saveToFile)

        self.undo_act = QAction(QIcon("images/undo.png"), "Скасувати")
        self.undo_act.setShortcut("Ctrl+Z")
        self.undo_act.triggered.connect(self.text_edit.undo)

    def createMenu(self):
        self.menuBar().setNativeMenuBar(False)

        file_menu = self.menuBar().addMenu("&Файл")
        file_menu.addAction(self.new_act)
        file_menu.addSeparator()
        file_menu.addAction(self.open_act)
        file_menu.addAction(self.save_act)
        file_menu.addSeparator()
        file_menu.addAction(self.quit_act)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

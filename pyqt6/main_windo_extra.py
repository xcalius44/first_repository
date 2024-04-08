import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QCheckBox,
    QTextEdit,
    QDockWidget,
    QToolBar,
    QStatusBar,
    QVBoxLayout,
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QIcon


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setMinimumSize(450, 350)
        self.setWindowTitle("MainWindow")
        self.setUpMainWindow()
        self.createDockWidget()
        self.createActions()
        self.createMenu()
        self.createToolBar()
        self.show()

    def setUpMainWindow(self):
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        self.setStatusBar(QStatusBar())

    def createActions(self):
        """Створення дій"""
        self.quit_act = QAction(QIcon("images/exit.png"), "&Вихід")
        self.quit_act.setShortcut("Ctrl+Q")
        self.quit_act.setStatusTip("Вихід з програми")
        self.quit_act.triggered.connect(self.close)

        self.full_screen_act = QAction("На весь екран", checkable=True)
        self.full_screen_act.setStatusTip("Перейти в режим на весь екран")
        self.full_screen_act.triggered.connect(self.switchToFullScreen)

    def createMenu(self):
        """Налаштування меню"""
        self.menuBar().setNativeMenuBar(False)

        file_menu = self.menuBar().addMenu("&Файл")
        file_menu.addAction(self.quit_act)

        view_menu = self.menuBar().addMenu("Перегляд")
        apperance_submenu = view_menu.addMenu("Зовнішній вигляд")
        apperance_submenu.addAction(self.full_screen_act)

    def switchToFullScreen(self, state):
        if state:
            self.showFullScreen()
        else:
            self.showNormal()

    def createToolBar(self):
        toolbar = QToolBar("Головна панель інструментів")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        toolbar.addAction(self.quit_act)

    def createDockWidget(self):
        dock_widget = QDockWidget()
        dock_widget.setWindowTitle("Форматування")
        dock_widget.setAllowedAreas(Qt.DockWidgetArea.AllDockWidgetAreas)

        auto_bullet_cb = QCheckBox("Автоматичний неупорядкований список")
        auto_bullet_cb.toggled.connect(self.changeTextEditSettings)

        dock_v_box = QVBoxLayout()
        dock_v_box.addWidget(auto_bullet_cb)
        dock_v_box.addStretch(1)

        dock_container = QWidget()
        dock_container.setLayout(dock_v_box)

        dock_widget.setWidget(dock_container)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, dock_widget)

    def changeTextEditSettings(self, checked):
        if checked:
            self.text_edit.setAutoFormatting(
                QTextEdit.AutoFormattingFlag.AutoBulletList
            )
        else:
            self.text_edit.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoNone)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

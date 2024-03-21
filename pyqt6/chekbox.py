import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QCheckBox
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    """Клас для головного вікна"""

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Налаштування застосунку"""
        self.setGeometry(100, 100, 250, 150)
        self.setWindowTitle("QChackBox Example")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        header_label = QLabel(
            "Які Python-бібліотеки Ви знаєте? (Будь ласка, позначте все, що використовували)",
            self,
        )
        header_label.setWordWrap(True)
        header_label.move(20, 20)

        pygame_cb = QCheckBox("PyGame", self)
        pygame_cb.move(40, 60)
        pygame_cb.toggled.connect(self.printSelected)

        pyqt_cb = QCheckBox("PyQt", self)
        pyqt_cb.move(40, 80)
        pyqt_cb.toggled.connect(self.printSelected)

        django_cb = QCheckBox("Django", self)
        django_cb.move(40, 100)
        django_cb.toggled.connect(self.printSelected)

    def printSelected(self, checked):
        """Виводе стан ChckBox"""
        sender = self.sender()
        if checked:
            print(f"{sender.text()} обрано")
        else:
            print(f"{sender.text()} не обрано")


# Запуск програми
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

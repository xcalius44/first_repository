import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QCheckBox,
    QPushButton,
    QButtonGroup,
    QVBoxLayout,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setMinimumSize(350, 200)
        self.setWindowTitle("QVBoxLayout Example")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        first_label = QLabel("Python-бібліотеки")
        first_label.setFont(QFont("Arial", 18))
        first_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header_label = QLabel(
            "Які Python-бібліотеки Ви знаєте? (Будь ласка, позначте все, що використовували)"
        )
        header_label.setWordWrap(True)
        header_label.setAlignment(Qt.AlignmentFlag.AlignTop)

        libraries = ("PyGame", "PyQt", "Django")
        libraries_group = QButtonGroup(self)
        libraries_group.buttonClicked.connect(self.printSelected)

        self.confirm_button = QPushButton("Підтвердити")
        self.confirm_button.setEnabled(False)
        self.confirm_button.clicked.connect(self.close)

        main_v_box = QVBoxLayout()
        main_v_box.addWidget(first_label)
        main_v_box.addWidget(header_label)

        for lib in libraries:
            cb = QCheckBox(lib)
            libraries_group.addButton(cb)
            main_v_box.addWidget(cb)

        main_v_box.addWidget(self.confirm_button)
        self.setLayout(main_v_box)

    def printSelected(self, button):
        print(f"{button.text()} обрано")
        self.confirm_button.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

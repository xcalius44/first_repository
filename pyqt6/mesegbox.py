import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QMessageBox,
    QLineEdit,
    QPushButton,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 340, 140)
        self.setWindowTitle("QMessageBox")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        catalog_label = QLabel("Каталог авторів", self)
        catalog_label.move(100, 10)
        catalog_label.setFont(QFont("Arial", 18))

        search_label = QLabel("Пошук автора по індексу:", self)
        search_label.move(20, 40)

        author_label = QLabel("Ім'я", self)
        author_label.move(20, 74)

        self.author_edit = QLineEdit(self)
        self.author_edit.move(70, 70)
        self.author_edit.resize(240, 24)
        self.author_edit.setPlaceholderText("Введіть автора як Ім'я Прізвище")

        search_button = QPushButton("Пошук", self)
        search_button.move(140, 100)
        search_button.clicked.connect(self.searchAuthors)

    def searchAuthors(self):
        file = "files/authors.txt"

        try:
            with open(file, encoding="UTF8") as f:
                authors = [s.rstrip("\n") for s in f]

            if self.author_edit.text() in authors:
                QMessageBox.information(
                    self,
                    "Автора знайдено",
                    "Автора знайдено в каталозі!",
                    QMessageBox.StandardButton.Ok,
                )
            else:
                answer = QMessageBox.question(
                    self,
                    "Автора не знайдено",
                    """<p>Автора не знайдено в каталозі.</p>
                    <p>Ви бажаєте продовжити?</p>""",
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                    QMessageBox.StandardButton.No,
                )
                if answer == QMessageBox.StandardButton.No:
                    print("Застосунок закрито.")
                    self.close()
        except FileNotFoundError as error:
            QMessageBox.warning(
                self,
                "Помилка",
                f"""<p>Файл не знайдено.</p>
                <p>Trror: {error}</p>
                Закриття застосунку.""",
                QMessageBox.StandardButton.Ok,
            )
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

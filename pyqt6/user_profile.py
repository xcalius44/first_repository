import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QFont, QPixmap


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(50, 50, 250, 400)
        self.setWindowTitle("User Profile GUI")
        self.setUpMainWindow()
        self.show()

    def createImageLabels(self):
        images = ["images/skyblue.png", "images/profile_image.png"]
        for image in images:
            try:
                with open(image):
                    label = QLabel(self)
                    pixmap = QPixmap(image)
                    label.setPixmap(pixmap)
                    if "profile" in image:
                        label.move(80, 20)
            except FileNotFoundError as error:
                print(f"Image no found.\nError: {error}")

    def setUpMainWindow(self):
        self.createImageLabels()

        user_label = QLabel(self)
        user_label.setText("Роман Яценко")
        user_label.setFont(QFont("Arial", 20))
        user_label.move(55, 140)

        bio_label = QLabel(self)
        bio_label.setText("Біографія")
        bio_label.setFont(QFont("Arial", 17))
        bio_label.move(15, 170)

        about_label = QLabel(self)
        about_label.setText(
            "Я - викладач програмування з 20-річним досвідом. Полюбляю Python"
        )
        about_label.setWordWrap(True)
        about_label.move(15, 195)

        skills_label = QLabel(self)
        skills_label.setText("Технології")
        skills_label.setFont(QFont("Arial", 17))
        skills_label.move(15, 240)

        languages_label = QLabel(self)
        languages_label.setText("Python | PyGame | PyQt | Django")
        languages_label.move(15, 265)

        experience_label = QLabel(self)
        experience_label.setText("Досвід")
        experience_label.setFont(QFont("Arial", 17))
        experience_label.move(15, 290)

        developer_label = QLabel(self)
        developer_label.setText("Python-Розробник")
        developer_label.move(15, 320)

        dev_dates_label = QLabel(self)
        dev_dates_label.setText("Вересень 2022 - по теперішній час")
        dev_dates_label.setFont(QFont("Arial", 10))
        dev_dates_label.move(15, 340)

        html_label = QLabel(self)
        html_label.setText("HTML-Верстальник")
        html_label.move(15, 360)

        html_dates_label = QLabel(self)
        html_dates_label.setText("Січень 2020 - Травень 2022")
        html_dates_label.setFont(QFont("Arial", 10))
        html_dates_label.move(15, 380)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

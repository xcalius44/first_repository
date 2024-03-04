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
        images = ["skyblue.png", "profile_image.png"]
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
        user_label.setText("Roman Yatsenko")
        user_label.setFont(QFont("Arial", 20))
        user_label.move(85, 140)

        bio_label = QLabel(self)
        bio_label.setText("Biography")
        bio_label.setFont(QFont("Arial", 17))
        bio_label.move(15, 170)

        about_label = QLabel(self)
        about_label.setText(
            "I am a programming teacher with 20 years of experience_ I love Python"
        )
        about_label.setWordWrap(True)
        about_label.move(15, 100)

        skills_label = QLabel(self)
        skills_label.setText("thno")
        skills_label.setFont(QFont("Arial", 17))
        skills_label.move(15, 240)

        languages_label = QLabel(self)
        languages_label.setText("Python | PyGame | PyQt | Django")
        languages_label.move(15, 268)

        experience_label = QLabel(self)
        experience_label.setText("Experience")
        experience_label.setFont(QFont("Arial", 17))
        experience_label.move(15, 290)

        developer_label = QLabel(self)
        developer_label.setText("Python-Developer")
        developer_label.move(15, 310)

        dev_dates_label = QLabel(self)
        dev_dates_label.setText("September 2022 to present")
        dev_dates_label.setFont(QFont("Arial", 10))
        developer_label.move(15, 330)

        html_label = QLabel(self)
        html_label.setText("HTML-Beрстальник")
        html_label.move(15, 350)

        html_dates_label = QLabel(self)
        html_dates_label.setText("January 2020 - May")
        html_dates_label.setFont(QFont("Arial", 10))
        html_dates_label.move(15, 330)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exit())

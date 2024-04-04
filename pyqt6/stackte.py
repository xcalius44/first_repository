import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QTextEdit,
    QComboBox,
    QSpinBox,
    QDoubleSpinBox,
    QStackedLayout,
    QFormLayout,
    QVBoxLayout,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setFixedSize(300, 340)
        self.setWindowTitle("QStackedLayout")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        page_combo = QComboBox()
        page_combo.addItems(["Зoбраження", "Опис", "Інформація"])
        page_combo.activated.connect(self.switchPage)

        # Page 1
        profile_image = QLabel()
        pixmap = QPixmap("images/norwegian.jpg")
        profile_image.setPixmap(pixmap)
        profile_image.setScaledContents(True)

        # Page 2
        pg2_form = QFormLayout()
        pg2_form.setFieldGrowthPolicy(pg2_form.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        pg2_form.setFormAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop
        )
        pg2_form.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)
        pg2_form.addRow("Порода:", QLabel("Норвезька лісова кішка"))
        pg2_form.addRow("Походження:", QLabel("Норвегія"))
        pg2_form.addRow(QLabel("Опис:"))
        text = """Порода кішок, що пропорціями свого тіла нагадує європейську короткошерсту. 
        Однак має одну особливість — довге водовідштовхувальне хутро, яке дуже швидко висихає після дощу.
        """
        pg2_form.addRow(QTextEdit(text))
        pg2_container = QWidget()
        pg2_container.setLayout(pg2_form)

        # Page 3
        pg3_form = QFormLayout()
        pg3_form.setFieldGrowthPolicy(pg3_form.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        pg3_form.setFormAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop
        )
        pg3_form.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)
        pg3_form.addRow(QLabel("Введіть інформацію прол Вашого котика"))
        pg3_form.addRow("Ім'я:", QLineEdit())
        pg3_form.addRow("Забарвлення:", QLineEdit())
        age_sb = QSpinBox()
        age_sb.setRange(0, 30)
        pg3_form.addRow("Вік:", age_sb)
        weight_dsb = QDoubleSpinBox()
        weight_dsb.setRange(0.0, 30.0)
        pg3_form.addRow("Вага:", weight_dsb)
        pg3_container = QWidget()
        pg3_container.setLayout(pg3_form)

        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(profile_image)
        self.stacked_layout.addWidget(pg2_container)
        self.stacked_layout.addWidget(pg3_container)
        main_v_box = QVBoxLayout()
        main_v_box.addWidget(page_combo)
        main_v_box.addLayout(self.stacked_layout)
        self.setLayout(main_v_box)

    def switchPage(self, index):
        self.stacked_layout.setCurrentIndex(index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

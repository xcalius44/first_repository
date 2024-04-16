import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QDockWidget,
    QFileDialog,
    QMessageBox,
    QToolBar,
    QStatusBar,
    QVBoxLayout,
    QDialog,
)
from PyQt6.QtCore import Qt, QSize, QRect
from PyQt6.QtGui import QAction, QIcon, QPixmap, QTransform, QPainter
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setFixedSize(650, 650)
        self.setWindowTitle("Photo Editor")
        self.setUpMainWindow()
        self.createToolsDockWidget()
        self.createActions()
        self.createMenu()
        self.createToolBar()
        self.show()

    def setUpMainWindow(self):
        self.image = QPixmap()

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.image_label)

        self.setStatusBar(QStatusBar())

    def createToolsDockWidget(self):
        dock_widget = QDockWidget()
        dock_widget.setWindowTitle("Редагування зображення")
        dock_widget.setAllowedAreas(
            Qt.DockWidgetArea.LeftDockWidgetArea | Qt.DockWidgetArea.RightDockWidgetArea
        )

        self.rotate90 = QPushButton("Повернути на 90°")
        self.rotate90.setMinimumSize(QSize(130, 40))
        self.rotate90.setStatusTip(
            "Повернути зображення на 90° за годиниковою стрілкою"
        )
        self.rotate90.clicked.connect(self.rotateImage90)

        self.rotate180 = QPushButton("Повернути на 180°")
        self.rotate180.setMinimumSize(QSize(130, 40))
        self.rotate180.setStatusTip(
            "Повернути зображення на 180° за годиниковою стрілкою"
        )
        self.rotate180.clicked.connect(self.rotateImage180)

        self.hor = QPushButton("Перевернути горизонтально")
        self.hor.setMinimumSize(QSize(130, 40))
        self.hor.setStatusTip("Перевернути зображення за горизонтальною віссю")
        self.hor.clicked.connect(self.flipImageHorizontal)

        self.ver = QPushButton("Перевернути вертикально")
        self.ver.setMinimumSize(QSize(130, 40))
        self.ver.setStatusTip("Перевернути зображення за вертикальною віссю")
        self.ver.clicked.connect(self.flipImageVertical)

        self.resize = QPushButton("Зменшити розмір вдвічі")
        self.resize.setMinimumSize(QSize(130, 40))
        self.resize.setStatusTip("Зменшення розміру зображення вдвічі")
        self.resize.clicked.connect(self.resizeImageHalf)

        dock_v_box = QVBoxLayout()
        dock_v_box.addWidget(self.rotate90)
        dock_v_box.addWidget(self.rotate180)
        dock_v_box.addStretch(1)
        dock_v_box.addWidget(self.hor)
        dock_v_box.addWidget(self.ver)
        dock_v_box.addStretch(1)
        dock_v_box.addWidget(self.resize)
        dock_v_box.addStretch(10)

        tools_container = QWidget()
        tools_container.setLayout(dock_v_box)
        dock_widget.setWidget(tools_container)

        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock_widget)

        self.toggle_doc_act = dock_widget.toggleViewAction()

    def createActions(self):
        self.quit_act = QAction("&Вихід")
        self.quit_act.setShortcut("Ctrl+Q")
        self.quit_act.setStatusTip("Вихід із програми")
        self.quit_act.triggered.connect(self.close)

        self.open_act = QAction(QIcon("images/open_file.png"), "Відкрити")
        self.open_act.setShortcut("Ctrl+O")
        self.open_act.setStatusTip("Відкрити нове зображення")
        self.open_act.triggered.connect(self.openImage)

        self.save_act = QAction(QIcon("images/save_file.png"), "Зберегти")
        self.save_act.setShortcut("Ctrl+S")
        self.save_act.setStatusTip("Зберегти зображення")
        self.save_act.triggered.connect(self.saveImage)

        self.print_act = QAction(QIcon("images/print.png"), "Друк")
        self.print_act.setShortcut("Ctrl+P")
        self.print_act.setStatusTip("Надрукувати зображення")
        self.print_act.triggered.connect(self.printImage)
        self.print_act.setEnabled(False)

        self.rotate90_act = QAction("Повернути на 90°")
        self.rotate90_act.setStatusTip(
            "Повернути зображення на 90° за годиниковою стрілкою"
        )
        self.rotate90_act.triggered.connect(self.rotateImage90)

        self.rotate180_act = QAction("Повернути на 180°")
        self.rotate180_act.setStatusTip(
            "Повернути зображення на 180° за годиниковою стрілкою"
        )
        self.rotate180_act.triggered.connect(self.rotateImage180)

        self.hor_act = QAction("Перевернути горизонтально")
        self.hor_act.setStatusTip("Перевернути зображення за горизонтальною віссю")
        self.hor_act.triggered.connect(self.flipImageHorizontal)

        self.ver_act = QAction("Перевернути вертикально")
        self.ver_act.setStatusTip("Перевернути зображення за вертикальною віссю")
        self.ver_act.triggered.connect(self.flipImageVertical)

        self.resize_act = QAction("Зменшити розмір вдвічі")
        self.resize_act.setStatusTip("Зменшення розміру зображення вдвічі")
        self.resize_act.triggered.connect(self.resizeImageHalf)

        self.clear_act = QAction(QIcon("images/clear.png"), "Очистити зображення")
        self.clear_act.setStatusTip("Очистити поточне зображення")
        self.clear_act.setShortcut("Ctrl+D")
        self.clear_act.triggered.connect(self.clearImage)

    def createMenu(self):
        self.menuBar().setNativeMenuBar(False)

        file_menu = self.menuBar().addMenu("&Файл")
        file_menu.addAction(self.open_act)
        file_menu.addAction(self.save_act)
        file_menu.addSeparator()
        file_menu.addAction(self.print_act)
        file_menu.addSeparator()
        file_menu.addAction(self.quit_act)

        edit_menu = self.menuBar().addMenu("Редагувати")
        edit_menu.addAction(self.rotate90_act)
        edit_menu.addAction(self.rotate180_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.hor_act)
        edit_menu.addAction(self.ver_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.resize_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.clear_act)

        view_menu = self.menuBar().addMenu("Перегляд")
        view_menu.addAction(self.toggle_doc_act)

    def createToolBar(self):
        tool_bar = QToolBar("Панель інструментів фоторедактора")
        tool_bar.setIconSize(QSize(24, 24))
        self.addToolBar(tool_bar)

        tool_bar.addAction(self.open_act)
        tool_bar.addAction(self.save_act)
        tool_bar.addAction(self.print_act)
        tool_bar.addAction(self.clear_act)
        tool_bar.addSeparator()
        tool_bar.addAction(self.quit_act)

    def openImage(self):
        image_file, _ = QFileDialog.getOpenFileName(
            self,
            "Відкрити зображення",
            "",
            "Графічні файли (*.jpeg *.jpg *.png *.bmp *.gif)",
        )
        if image_file:
            self.image = QPixmap(image_file)
            self.image_label.setPixmap(
                self.image.scaled(
                    self.image_label.size(),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )
            self.print_act.setEnabled(True)
        else:
            QMessageBox.information(
                self,
                "Відсутнє зображення",
                "Зображення не вибрано",
                QMessageBox.StandardButton.Ok,
            )

    def saveImage(self):
        image_file, _ = QFileDialog.getSaveFileName(
            self,
            "Зберегти зображення",
            "",
            "Графічні файли (*.jpeg *.jpg *.png *.bmp *.gif)",
        )
        if image_file and not self.image.isNull():
            self.image.save(image_file)
        else:
            QMessageBox.information(
                self,
                "Не збережено",
                "Зображення не збережено",
                QMessageBox.StandardButton.Ok,
            )

    def clearImage(self):
        self.image_label.clear()
        self.image = QPixmap()
        self.print_act.setEnabled(False)

    def rotateImage90(self):
        if not self.image.isNull():
            transform90 = QTransform().rotate(90)
            pixmap = QPixmap(self.image)
            mode = Qt.TransformationMode.SmoothTransformation
            rotated = pixmap.transformed(transform90, mode)
            self.image_label.setPixmap(
                rotated.scaled(
                    self.image_label.size(),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )
            self.image = QPixmap(rotated)
            self.image_label.repaint()

    def rotateImage180(self):
        if not self.image.isNull():
            transform90 = QTransform().rotate(180)
            pixmap = QPixmap(self.image)
            mode = Qt.TransformationMode.SmoothTransformation
            rotated = pixmap.transformed(transform90, mode)
            self.image_label.setPixmap(
                rotated.scaled(
                    self.image_label.size(),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )
            self.image = QPixmap(rotated)
            self.image_label.repaint()

    def flipImageHorizontal(self):
        if not self.image.isNull():
            flip_h = QTransform().scale(-1, 1)
            pixmap = QPixmap(self.image)
            flipped = pixmap.transformed(flip_h)
            self.image_label.setPixmap(
                flipped.scaled(
                    self.image_label.size(),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )
            self.image = QPixmap(flipped)
            self.image_label.repaint()

    def flipImageVertical(self):
        if not self.image.isNull():
            flip_v = QTransform().scale(1, -1)
            pixmap = QPixmap(self.image)
            flipped = pixmap.transformed(flip_v)
            self.image_label.setPixmap(
                flipped.scaled(
                    self.image_label.size(),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )
            self.image = QPixmap(flipped)
            self.image_label.repaint()

    def resizeImageHalf(self):
        if not self.image.isNull():
            flip_v = QTransform().scale(0.5, 0.5)
            pixmap = QPixmap(self.image)
            flipped = pixmap.transformed(flip_v)
            self.image_label.setPixmap(
                flipped.scaled(
                    self.image_label.size(),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )
            self.image = QPixmap(flipped)
            self.image_label.repaint()

    def printImage(self):
        printer = QPrinter()
        print_dilaog = QPrintDialog(printer)
        if print_dilaog.exec() == QDialog.DialogCode.Accepted:
            painter = QPainter()
            painter.begin(printer)
            rect = QRect(painter.viewport())
            size = QSize(self.image_label.pixmap().size())
            size.scale(rect.size(), Qt.AspectRatioMode.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.image_label.pixmap().rect())
            painter.drawPixmap(0, 0, self.image_label.pixmap())
            painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setAttribute(Qt.ApplicationAttribute.AA_DontShowIconsInMenus, True)
    window = MainWindow()
    sys.exit(app.exec())

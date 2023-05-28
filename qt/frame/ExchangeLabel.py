from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QApplication, QMainWindow


# 重写Label 实现点击图片
class ExchangeLabel(QMainWindow):
    def __init__(self):
        self = QMainWindow.exchangeLabel

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.parent().exchange_combox_select()
            print(self.parent() + "running")

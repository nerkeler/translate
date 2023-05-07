import sys
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow
from qt.frame.TranslateFrame import Ui_MainWindow
from utils.baiduApi import baiduTranslate


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 实现点击图片 调用自定义方法
        self.exchangeLabel.mousePressEvent = self.on_label_clicked
        self.clearLlabel.mousePressEvent = self.chearText
        self.timer = QTimer()
        # 定时器，超过时间间隔才会请求
        self.timer.setInterval(250)  # 设置时间间隔为250ms
        self.timer.timeout.connect(self.on_timer_timeout)

    # 交换 目标语言和源语言
    def on_label_clicked(self, event):
        if event.button() == Qt.LeftButton:
            source = self.sourceComboBox.currentText()
            target = self.targetComboBox.currentText()
            self.sourceComboBox.setCurrentText(target)
            self.targetComboBox.setCurrentText(source)

    def queryBaiduApi(self):
        self.on_text_changed()

    def chearText(self, event):
        if event.button() == Qt.LeftButton:
            self.sourceTextEdit.clear()
            self.targetTextEdit.clear()

    # 定时器超时触发请求
    def on_timer_timeout(self):
        self.timer.stop()
        source = self.sourceComboBox.currentText()
        target = self.targetComboBox.currentText()
        query = self.sourceTextEdit.toPlainText()
        if query is not None and query.strip() != '':
            self.queryText = query
            result = baiduTranslate(source, target, query)
            self.targetTextEdit.clear()
            trans_result = result['trans_result']
            target_result = ''
            for item in trans_result:
                target_result = target_result + item['dst'] + '\n'

            self.targetTextEdit.setText(target_result)

    def on_text_changed(self):
        self.timer.start()  # 每次输入内容时重新启动计时器


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())

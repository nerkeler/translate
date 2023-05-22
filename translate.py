import sys
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow

from mapper.WordRecord import WordRecord
from qt.frame.TranslateFrame import Ui_MainWindow
from utils.baiduApi import baiduTranslate
import pyperclip
import pyttsx3


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 实现点击图片 调用自定义方法
        self.exchangeLabel.mousePressEvent = self.on_label_clicked
        self.clearLlabel.mousePressEvent = self.chearText
        self.copyLabel.mousePressEvent = self.copyToBoard
        self.pasteLabel.mousePressEvent = self.pasteToEdit
        self.speakerLabel1.mousePressEvent = self.speakerSourceText
        self.speakerLabel2.mousePressEvent = self.speakerTargetText
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

    def copyToBoard(self, event):
        if event.button() == Qt.LeftButton:
            text = self.targetTextEdit.toPlainText()
            pyperclip.copy(text)

    def pasteToEdit(self, event):
        if event.button() == Qt.LeftButton:
            text = pyperclip.paste()
            self.sourceTextEdit.setText(text)

    def speakerSourceText(self, event):
        if event.button() == Qt.LeftButton:
            text = self.sourceTextEdit.toPlainText()

            engine = pyttsx3.init()
            engine.setProperty('rate', 150)  # 设置语速
            # engine.setProperty('volume', 0.9)  # 设置音量
            # voices = engine.getProperty('voices')
            # engine.setProperty('voice', voices[1].id)  # 设置声音（这里指定第二种中文女声）
            engine.say(text)
            engine.runAndWait()


    def speakerTargetText(self, event):
        text = self.targetTextEdit.toPlainText()
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # 设置语速
        # engine.setProperty('volume', 0.9)  # 设置音量
        # voices = engine.getProperty('voices')
        # engine.setProperty('voice', 'english')
        # engine.setProperty('voice', voices[1].id)  # 设置声音（这里指定第二种中文女声）
        engine.say(text)
        engine.runAndWait()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())

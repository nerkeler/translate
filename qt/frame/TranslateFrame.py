# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TranslateUi.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QMainWindow, QSizePolicy, QTextEdit, QWidget)
import qt.resource.resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(569, 514)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.sourceComboBox = QComboBox(self.centralwidget)
        self.sourceComboBox.addItem("")
        self.sourceComboBox.addItem("")
        self.sourceComboBox.addItem("")
        self.sourceComboBox.addItem("")
        self.sourceComboBox.addItem("")
        self.sourceComboBox.addItem("")
        self.sourceComboBox.setObjectName(u"sourceComboBox")
        self.sourceComboBox.setGeometry(QRect(80, 80, 91, 31))
        self.sourceComboBox.setMaximumSize(QSize(16777215, 110))
        font = QFont()
        font.setPointSize(10)
        self.sourceComboBox.setFont(font)
        self.targetComboBox = QComboBox(self.centralwidget)
        self.targetComboBox.addItem("")
        self.targetComboBox.addItem("")
        self.targetComboBox.addItem("")
        self.targetComboBox.addItem("")
        self.targetComboBox.addItem("")
        self.targetComboBox.addItem("")
        self.targetComboBox.setObjectName(u"targetComboBox")
        self.targetComboBox.setGeometry(QRect(390, 80, 91, 31))
        self.targetComboBox.setMaximumSize(QSize(16777215, 110))
        self.targetComboBox.setFont(font)
        self.exchangeLabel = QLabel(self.centralwidget)
        self.exchangeLabel.setObjectName(u"exchangeLabel")
        self.exchangeLabel.setGeometry(QRect(220, 70, 111, 51))
        self.exchangeLabel.setMaximumSize(QSize(16777215, 110))
        self.exchangeLabel.setPixmap(QPixmap(u":/resource/bidirectional.png"))
        self.exchangeLabel.setScaledContents(True)
        self.sourceTextEdit = QTextEdit(self.centralwidget)
        self.sourceTextEdit.setObjectName(u"sourceTextEdit")
        self.sourceTextEdit.setGeometry(QRect(70, 160, 201, 261))
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(16)
        self.sourceTextEdit.setFont(font1)
        self.targetTextEdit = QTextEdit(self.centralwidget)
        self.targetTextEdit.setObjectName(u"targetTextEdit")
        self.targetTextEdit.setGeometry(QRect(290, 160, 201, 261))
        self.targetTextEdit.setFont(font1)
        self.speakerLabel = QLabel(self.centralwidget)
        self.speakerLabel.setObjectName(u"speakerLabel")
        self.speakerLabel.setGeometry(QRect(420, 440, 54, 41))
        self.speakerLabel.setPixmap(QPixmap(u":/resource/speakers.png"))
        self.speakerLabel.setScaledContents(True)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(80, 130, 401, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.clearLlabel = QLabel(self.centralwidget)
        self.clearLlabel.setObjectName(u"clearLlabel")
        self.clearLlabel.setGeometry(QRect(260, 150, 21, 21))
        self.clearLlabel.setPixmap(QPixmap(u":/resource/close.png"))
        self.clearLlabel.setScaledContents(True)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(270, 160, 20, 261))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        MainWindow.setCentralWidget(self.centralwidget)
        self.sourceTextEdit.raise_()
        self.sourceComboBox.raise_()
        self.targetComboBox.raise_()
        self.exchangeLabel.raise_()
        self.targetTextEdit.raise_()
        self.speakerLabel.raise_()
        self.line_2.raise_()
        self.line.raise_()
        self.clearLlabel.raise_()

        self.retranslateUi(MainWindow)
        self.sourceTextEdit.textChanged.connect(MainWindow.queryBaiduApi)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.sourceComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u7b80\u4f53\u4e2d\u6587", None))
        self.sourceComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"AUTO", None))
        self.sourceComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u82f1\u8bed", None))
        self.sourceComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u7e41\u4f53\u4e2d\u6587", None))
        self.sourceComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\u65e5\u8bed", None))
        self.sourceComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"\u7ca4\u8bed", None))

        self.targetComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u82f1\u8bed", None))
        self.targetComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"AUTO", None))
        self.targetComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u7b80\u4f53\u4e2d\u6587", None))
        self.targetComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u7e41\u4f53\u4e2d\u6587", None))
        self.targetComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\u7ca4\u8bed", None))
        self.targetComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"\u65e5\u8bed", None))

        self.exchangeLabel.setText("")
        self.sourceTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u6587\u672c", None))
        self.targetTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7ffb\u8bd1", None))
        self.speakerLabel.setText("")
        self.clearLlabel.setText("")
    # retranslateUi

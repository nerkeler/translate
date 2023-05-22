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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)
import qt.frame.resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(773, 624)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 2, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 45))
        self.frame_3.setMaximumSize(QSize(16777215, 45))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(83, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.sourceComboBox = QComboBox(self.frame_3)
        self.sourceComboBox.addItem("")
        self.sourceComboBox.addItem("")
        self.sourceComboBox.addItem("")
        self.sourceComboBox.addItem("")
        self.sourceComboBox.addItem("")
        self.sourceComboBox.addItem("")
        self.sourceComboBox.setObjectName(u"sourceComboBox")
        self.sourceComboBox.setMinimumSize(QSize(100, 31))
        self.sourceComboBox.setMaximumSize(QSize(100, 31))
        font = QFont()
        font.setPointSize(10)
        self.sourceComboBox.setFont(font)

        self.horizontalLayout_4.addWidget(self.sourceComboBox)

        self.horizontalSpacer_5 = QSpacerItem(84, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.exchangeLabel = QLabel(self.frame_3)
        self.exchangeLabel.setObjectName(u"exchangeLabel")
        self.exchangeLabel.setMinimumSize(QSize(111, 31))
        self.exchangeLabel.setMaximumSize(QSize(111, 31))
        self.exchangeLabel.setPixmap(QPixmap(u":/resource/bidirectional.png"))
        self.exchangeLabel.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.exchangeLabel)

        self.horizontalSpacer_6 = QSpacerItem(83, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.targetComboBox = QComboBox(self.frame_3)
        self.targetComboBox.addItem("")
        self.targetComboBox.addItem("")
        self.targetComboBox.addItem("")
        self.targetComboBox.addItem("")
        self.targetComboBox.addItem("")
        self.targetComboBox.addItem("")
        self.targetComboBox.setObjectName(u"targetComboBox")
        self.targetComboBox.setMinimumSize(QSize(100, 31))
        self.targetComboBox.setMaximumSize(QSize(100, 31))
        self.targetComboBox.setFont(font)

        self.horizontalLayout_4.addWidget(self.targetComboBox)

        self.horizontalSpacer_4 = QSpacerItem(83, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 31))
        self.frame.setMaximumSize(QSize(16777215, 31))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(242, 8, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.speakerLabel1 = QLabel(self.frame)
        self.speakerLabel1.setObjectName(u"speakerLabel1")
        self.speakerLabel1.setMinimumSize(QSize(21, 21))
        self.speakerLabel1.setMaximumSize(QSize(21, 21))
        self.speakerLabel1.setPixmap(QPixmap(u":/resource/speakers.png"))
        self.speakerLabel1.setScaledContents(True)

        self.horizontalLayout.addWidget(self.speakerLabel1)

        self.pasteLabel = QLabel(self.frame)
        self.pasteLabel.setObjectName(u"pasteLabel")
        self.pasteLabel.setMinimumSize(QSize(21, 21))
        self.pasteLabel.setMaximumSize(QSize(21, 21))
        self.pasteLabel.setPixmap(QPixmap(u":/resource/paste.png"))
        self.pasteLabel.setScaledContents(True)

        self.horizontalLayout.addWidget(self.pasteLabel)

        self.clearLlabel = QLabel(self.frame)
        self.clearLlabel.setObjectName(u"clearLlabel")
        self.clearLlabel.setMinimumSize(QSize(21, 21))
        self.clearLlabel.setMaximumSize(QSize(21, 21))
        self.clearLlabel.setPixmap(QPixmap(u":/resource/close.png"))
        self.clearLlabel.setScaledContents(True)

        self.horizontalLayout.addWidget(self.clearLlabel)


        self.verticalLayout_2.addWidget(self.frame)

        self.sourceTextEdit = QTextEdit(self.centralwidget)
        self.sourceTextEdit.setObjectName(u"sourceTextEdit")
        self.sourceTextEdit.setMinimumSize(QSize(200, 260))
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(16)
        self.sourceTextEdit.setFont(font1)

        self.verticalLayout_2.addWidget(self.sourceTextEdit)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 30))
        self.frame_2.setMaximumSize(QSize(16777215, 30))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacerTrans = QSpacerItem(241, 7, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacerTrans)

        self.speakerLabel2 = QLabel(self.frame_2)
        self.speakerLabel2.setObjectName(u"speakerLabel2")
        self.speakerLabel2.setMinimumSize(QSize(21, 21))
        self.speakerLabel2.setMaximumSize(QSize(21, 21))
        self.speakerLabel2.setPixmap(QPixmap(u":/resource/speakers.png"))
        self.speakerLabel2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.speakerLabel2)

        self.copyLabel = QLabel(self.frame_2)
        self.copyLabel.setObjectName(u"copyLabel")
        self.copyLabel.setMinimumSize(QSize(21, 21))
        self.copyLabel.setMaximumSize(QSize(21, 21))
        self.copyLabel.setPixmap(QPixmap(u":/resource/copy.png"))
        self.copyLabel.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.copyLabel)

        self.clearLlabel_2 = QLabel(self.frame_2)
        self.clearLlabel_2.setObjectName(u"clearLlabel_2")
        self.clearLlabel_2.setMinimumSize(QSize(21, 21))
        self.clearLlabel_2.setMaximumSize(QSize(21, 21))
        self.clearLlabel_2.setPixmap(QPixmap(u":/resource/close.png"))
        self.clearLlabel_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.clearLlabel_2)

        self.clearLlabel_2.raise_()
        self.copyLabel.raise_()
        self.speakerLabel2.raise_()

        self.verticalLayout.addWidget(self.frame_2)

        self.targetTextEdit = QTextEdit(self.centralwidget)
        self.targetTextEdit.setObjectName(u"targetTextEdit")
        self.targetTextEdit.setMinimumSize(QSize(200, 260))
        self.targetTextEdit.setFont(font1)

        self.verticalLayout.addWidget(self.targetTextEdit)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

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

        self.exchangeLabel.setText("")
        self.targetComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u82f1\u8bed", None))
        self.targetComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"AUTO", None))
        self.targetComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u7b80\u4f53\u4e2d\u6587", None))
        self.targetComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u7e41\u4f53\u4e2d\u6587", None))
        self.targetComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\u7ca4\u8bed", None))
        self.targetComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"\u65e5\u8bed", None))

        self.speakerLabel1.setText("")
        self.pasteLabel.setText("")
        self.clearLlabel.setText("")
        self.sourceTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u6587\u672c", None))
        self.speakerLabel2.setText("")
        self.copyLabel.setText("")
        self.clearLlabel_2.setText("")
        self.targetTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7ffb\u8bd1", None))
    # retranslateUi


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
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)
import qt.resource.resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(955, 565)
        MainWindow.setMaximumSize(QSize(955, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(955, 16777215))
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.source_frame = QFrame(self.frame_3)
        self.source_frame.setObjectName(u"source_frame")
        self.source_frame.setFrameShape(QFrame.StyledPanel)
        self.source_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.source_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.source_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(260, 0))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(242, 8, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.speakerLabel1 = QLabel(self.frame_5)
        self.speakerLabel1.setObjectName(u"speakerLabel1")
        self.speakerLabel1.setMinimumSize(QSize(21, 21))
        self.speakerLabel1.setMaximumSize(QSize(21, 21))
        self.speakerLabel1.setPixmap(QPixmap(u":/resource/speakers.png"))
        self.speakerLabel1.setScaledContents(True)

        self.horizontalLayout.addWidget(self.speakerLabel1)

        self.pasteLabel = QLabel(self.frame_5)
        self.pasteLabel.setObjectName(u"pasteLabel")
        self.pasteLabel.setMinimumSize(QSize(21, 21))
        self.pasteLabel.setMaximumSize(QSize(21, 21))
        self.pasteLabel.setPixmap(QPixmap(u":/resource/paste.png"))
        self.pasteLabel.setScaledContents(True)

        self.horizontalLayout.addWidget(self.pasteLabel)

        self.clearLlabel = QLabel(self.frame_5)
        self.clearLlabel.setObjectName(u"clearLlabel")
        self.clearLlabel.setMinimumSize(QSize(21, 21))
        self.clearLlabel.setMaximumSize(QSize(21, 21))
        self.clearLlabel.setPixmap(QPixmap(u":/resource/close.png"))
        self.clearLlabel.setScaledContents(True)

        self.horizontalLayout.addWidget(self.clearLlabel)


        self.verticalLayout.addWidget(self.frame_5)

        self.sourceTextEdit = QTextEdit(self.source_frame)
        self.sourceTextEdit.setObjectName(u"sourceTextEdit")
        self.sourceTextEdit.setMinimumSize(QSize(200, 260))
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(16)
        self.sourceTextEdit.setFont(font)

        self.verticalLayout.addWidget(self.sourceTextEdit)


        self.gridLayout.addWidget(self.source_frame, 1, 0, 1, 1)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.target_frame = QFrame(self.frame_4)
        self.target_frame.setObjectName(u"target_frame")
        self.target_frame.setMinimumSize(QSize(260, 0))
        self.target_frame.setFrameShape(QFrame.StyledPanel)
        self.target_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.target_frame)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacerTrans = QSpacerItem(242, 8, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacerTrans)

        self.speakerLabel2 = QLabel(self.target_frame)
        self.speakerLabel2.setObjectName(u"speakerLabel2")
        self.speakerLabel2.setMinimumSize(QSize(21, 21))
        self.speakerLabel2.setMaximumSize(QSize(21, 21))
        self.speakerLabel2.setPixmap(QPixmap(u":/resource/speakers.png"))
        self.speakerLabel2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.speakerLabel2)

        self.copyLabel = QLabel(self.target_frame)
        self.copyLabel.setObjectName(u"copyLabel")
        self.copyLabel.setMinimumSize(QSize(21, 21))
        self.copyLabel.setMaximumSize(QSize(21, 21))
        self.copyLabel.setPixmap(QPixmap(u":/resource/copy.png"))
        self.copyLabel.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.copyLabel)

        self.clearLlabel_2 = QLabel(self.target_frame)
        self.clearLlabel_2.setObjectName(u"clearLlabel_2")
        self.clearLlabel_2.setMinimumSize(QSize(21, 21))
        self.clearLlabel_2.setMaximumSize(QSize(21, 21))
        self.clearLlabel_2.setPixmap(QPixmap(u":/resource/close.png"))
        self.clearLlabel_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.clearLlabel_2)


        self.verticalLayout_2.addWidget(self.target_frame)

        self.targetTextEdit = QTextEdit(self.frame_4)
        self.targetTextEdit.setObjectName(u"targetTextEdit")
        self.targetTextEdit.setMinimumSize(QSize(200, 260))
        self.targetTextEdit.setFont(font)

        self.verticalLayout_2.addWidget(self.targetTextEdit)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.top_frame = QFrame(self.frame_3)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMinimumSize(QSize(0, 45))
        self.top_frame.setMaximumSize(QSize(16777215, 45))
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(83, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.sourceComboBox = QComboBox(self.top_frame)
        self.sourceComboBox.addItem("")
        self.sourceComboBox.addItem("")
        self.sourceComboBox.addItem("")
        self.sourceComboBox.addItem("")
        self.sourceComboBox.addItem("")
        self.sourceComboBox.addItem("")
        self.sourceComboBox.setObjectName(u"sourceComboBox")
        self.sourceComboBox.setMinimumSize(QSize(100, 31))
        self.sourceComboBox.setMaximumSize(QSize(100, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.sourceComboBox.setFont(font1)

        self.horizontalLayout_4.addWidget(self.sourceComboBox)

        self.horizontalSpacer_5 = QSpacerItem(84, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.exchangeLabel = QLabel(self.top_frame)
        self.exchangeLabel.setObjectName(u"exchangeLabel")
        self.exchangeLabel.setMinimumSize(QSize(111, 25))
        self.exchangeLabel.setMaximumSize(QSize(111, 25))
        self.exchangeLabel.setPixmap(QPixmap(u":/resource/bidirectional.png"))
        self.exchangeLabel.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.exchangeLabel)

        self.horizontalSpacer_6 = QSpacerItem(83, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.targetComboBox = QComboBox(self.top_frame)
        self.targetComboBox.addItem("")
        self.targetComboBox.addItem("")
        self.targetComboBox.addItem("")
        self.targetComboBox.addItem("")
        self.targetComboBox.addItem("")
        self.targetComboBox.addItem("")
        self.targetComboBox.setObjectName(u"targetComboBox")
        self.targetComboBox.setMinimumSize(QSize(100, 31))
        self.targetComboBox.setMaximumSize(QSize(100, 31))
        self.targetComboBox.setFont(font1)

        self.horizontalLayout_4.addWidget(self.targetComboBox)

        self.horizontalSpacer_4 = QSpacerItem(83, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.fold_label = QLabel(self.top_frame)
        self.fold_label.setObjectName(u"fold_label")
        self.fold_label.setMinimumSize(QSize(31, 31))
        self.fold_label.setMaximumSize(QSize(31, 31))
        self.fold_label.setPixmap(QPixmap(u":/resource/fold.png"))
        self.fold_label.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.fold_label)


        self.gridLayout.addWidget(self.top_frame, 0, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 2, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(11)
        self.label.setFont(font2)

        self.verticalLayout_3.addWidget(self.label)

        self.history_list = QListWidget(self.frame_2)
        self.history_list.setObjectName(u"history_list")
        self.history_list.setMinimumSize(QSize(230, 0))
        self.history_list.setMaximumSize(QSize(230, 16777215))
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(False)
        self.history_list.setFont(font3)

        self.verticalLayout_3.addWidget(self.history_list)


        self.horizontalLayout_3.addWidget(self.frame_2)


        self.gridLayout_2.addWidget(self.frame, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.sourceTextEdit.textChanged.connect(MainWindow.queryBaiduApi)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.speakerLabel1.setText("")
        self.pasteLabel.setText("")
        self.clearLlabel.setText("")
        self.sourceTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u6587\u672c", None))
        self.speakerLabel2.setText("")
        self.copyLabel.setText("")
        self.clearLlabel_2.setText("")
        self.targetTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7ffb\u8bd1", None))
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

        self.fold_label.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u5386\u53f2", None))
    # retranslateUi


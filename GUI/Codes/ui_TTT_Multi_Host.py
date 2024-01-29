# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TTT_Multi_HostfsfaMq.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        font = QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 801, 81))
        font1 = QFont()
        font1.setFamilies([u"Arial Black"])
        font1.setPointSize(32)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setKerning(True)
        self.label.setFont(font1)
        self.label.setTextFormat(Qt.PlainText)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 100, 741, 431))
        font2 = QFont()
        font2.setBold(False)
        font2.setItalic(False)
        font2.setKerning(True)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.frame.setFont(font2)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"background-color: rgb(208, 208, 208);")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Plain)
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(30, 320, 681, 61))
        font3 = QFont()
        font3.setPointSize(15)
        font3.setBold(False)
        self.pushButton_3.setFont(font3)
        self.pushButton_3.setStyleSheet(u"background-color: rgb(177, 177, 177);")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 20, 681, 41))
        font4 = QFont()
        font4.setFamilies([u"Copperplate Gothic Bold"])
        font4.setPointSize(30)
        font4.setBold(True)
        font4.setItalic(False)
        font4.setKerning(True)
        self.label_3.setFont(font4)
        self.label_3.setTextFormat(Qt.PlainText)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 120, 681, 61))
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(15)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setKerning(True)
        self.label_4.setFont(font5)
        self.label_4.setTextFormat(Qt.PlainText)
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.plainTextEdit = QPlainTextEdit(self.frame)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(30, 180, 681, 61))
        font6 = QFont()
        font6.setFamilies([u"Arial Black"])
        font6.setPointSize(25)
        font6.setItalic(True)
        self.plainTextEdit.setFont(font6)
        self.plainTextEdit.setBackgroundVisible(False)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 270, 681, 41))
        font7 = QFont()
        font7.setFamilies([u"Arial"])
        font7.setPointSize(12)
        font7.setBold(False)
        font7.setItalic(False)
        font7.setKerning(True)
        self.label_5.setFont(font7)
        self.label_5.setStyleSheet(u"color: rgb(211, 0, 4);")
        self.label_5.setTextFormat(Qt.PlainText)
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tic Tac Toe - LAN", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Tic Tac Toe", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Spiel starten", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Multiplayer -- Host a game", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Gib einen Port ein auf dem das Spiel gehostet werden soll (>50000):", None))
        self.plainTextEdit.setDocumentTitle("")
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"55555", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Fehlermeldung: Error", None))
    # retranslateUi

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.show()
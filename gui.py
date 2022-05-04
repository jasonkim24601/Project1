# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designervDNLvi.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 400)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.rButton_rock = QRadioButton(self.centralwidget)
        self.rButton_rock.setObjectName(u"rButton_rock")
        self.rButton_rock.setGeometry(QRect(160, 220, 82, 17))
        self.rButton_paper = QRadioButton(self.centralwidget)
        self.rButton_paper.setObjectName(u"rButton_paper")
        self.rButton_paper.setGeometry(QRect(160, 240, 82, 17))
        self.rButton_scissors = QRadioButton(self.centralwidget)
        self.rButton_scissors.setObjectName(u"rButton_scissors")
        self.rButton_scissors.setGeometry(QRect(160, 260, 82, 17))
        self.pButton_submit = QPushButton(self.centralwidget)
        self.pButton_submit.setObjectName(u"pButton_submit")
        self.pButton_submit.setGeometry(QRect(160, 280, 75, 23))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 20, 371, 61))
        font = QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(280, 310, 61, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(250, 330, 101, 16))
        self.label_playerscore = QLabel(self.centralwidget)
        self.label_playerscore.setObjectName(u"label_playerscore")
        self.label_playerscore.setGeometry(QRect(340, 310, 47, 13))
        self.label_cpuscore = QLabel(self.centralwidget)
        self.label_cpuscore.setObjectName(u"label_cpuscore")
        self.label_cpuscore.setGeometry(QRect(340, 330, 47, 13))
        self.label_events = QLabel(self.centralwidget)
        self.label_events.setObjectName(u"label_events")
        self.label_events.setGeometry(QRect(80, 100, 231, 91))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.rButton_rock.setText(QCoreApplication.translate("MainWindow", u"Rock", None))
        self.rButton_paper.setText(QCoreApplication.translate("MainWindow", u"Paper", None))
        self.rButton_scissors.setText(QCoreApplication.translate("MainWindow", u"Scissors", None))
        self.pButton_submit.setText(QCoreApplication.translate("MainWindow", u"GO!", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Rock Paper Scissors!", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Your Score:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Computer's Score:", None))
        self.label_playerscore.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_cpuscore.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_events.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi


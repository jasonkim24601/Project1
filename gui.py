# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.rButton_rock = QtWidgets.QRadioButton(self.centralwidget)
        self.rButton_rock.setGeometry(QtCore.QRect(160, 220, 82, 17))
        self.rButton_rock.setObjectName("rButton_rock")
        self.rButton_paper = QtWidgets.QRadioButton(self.centralwidget)
        self.rButton_paper.setGeometry(QtCore.QRect(160, 240, 82, 17))
        self.rButton_paper.setObjectName("rButton_paper")
        self.rButton_scissors = QtWidgets.QRadioButton(self.centralwidget)
        self.rButton_scissors.setGeometry(QtCore.QRect(160, 260, 82, 17))
        self.rButton_scissors.setObjectName("rButton_scissors")



        self.pButton_submit = QtWidgets.QPushButton(self.centralwidget)
        self.pButton_submit.setGeometry(QtCore.QRect(160, 280, 75, 23))
        self.pButton_submit.setObjectName("pButton_submit")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 20, 371, 61))



        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 310, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 330, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_playerscore = QtWidgets.QLabel(self.centralwidget)
        self.label_playerscore.setGeometry(QtCore.QRect(340, 310, 47, 13))
        self.label_playerscore.setObjectName("label_playerscore")
        self.label_cpuscore = QtWidgets.QLabel(self.centralwidget)
        self.label_cpuscore.setGeometry(QtCore.QRect(340, 330, 47, 13))
        self.label_cpuscore.setObjectName("label_cpuscore")
        self.label_events = QtWidgets.QLabel(self.centralwidget)
        self.label_events.setGeometry(QtCore.QRect(80, 100, 231, 91))
        self.label_events.setObjectName("label_events")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.rButton_rock.setText(_translate("MainWindow", "Rock"))
        self.rButton_paper.setText(_translate("MainWindow", "Paper"))
        self.rButton_scissors.setText(_translate("MainWindow", "Scissors"))
        self.pButton_submit.setText(_translate("MainWindow", "GO!"))
        self.label.setText(_translate("MainWindow", "Rock Paper Scissors!"))
        self.label_2.setText(_translate("MainWindow", "Your Score:"))
        self.label_3.setText(_translate("MainWindow", "Computer\'s Score:"))
        self.label_playerscore.setText(_translate("MainWindow", "TextLabel"))
        self.label_cpuscore.setText(_translate("MainWindow", "TextLabel"))
        self.label_events.setText(_translate("MainWindow", "TextLabel"))






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

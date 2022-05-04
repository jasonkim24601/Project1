from PyQt5.QtWidgets import *
from gui import Ui_MainWindow
from rps import *


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.pButton_submit.clicked.connect(lambda : self.submit())

    def submit(self):
        playerChoice = None
        if self.rButton_rock.isChecked():
            playerChoice = 1
        if self.rButton_paper.isChecked():
            playerChoice = 2
        if self.rButton_scissors.isChecked():
            playerChoice = 3

        rps_result = rps(playerChoice)

        if rps_result == 0:
            self.label_events.setText("TIE")
        if rps_result == 1:
            self.label_events.setText("YOU WIN")
        if rps_result == 3:
            self.label_events.setText("CPU WIN")


from PyQt5.QtWidgets import *
from gui import Ui_MainWindow
from rps import *

global playerScore
playerScore = 0
global cpuScore
cpuScore = 0


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.pButton_submit.clicked.connect(lambda: self.submit())
        self.label_playerscore.setText(str(playerScore))
        self.label_playerscore.setText(str(cpuScore))

        # Start by hiding all the images
        self.label_cpu_rock.hide()
        self.label_cpu_paper.hide()
        self.label_cpu_scissor.hide()
        self.label_player_rock.hide()
        self.label_player_paper.hide()
        self.label_player_scissor.hide()

    def submit(self):

        self.label_cpu_rock.hide()
        self.label_cpu_paper.hide()
        self.label_cpu_scissor.hide()
        self.label_player_rock.hide()
        self.label_player_paper.hide()
        self.label_player_scissor.hide()

        playerChoice = 0
        playerChoiceText = 0

        global playerScore
        global cpuScore

        if self.rButton_rock.isChecked():
            playerChoice = 1

        if self.rButton_paper.isChecked():
            playerChoice = 2

        if self.rButton_scissors.isChecked():
            playerChoice = 3


        cpus_choice = cpu_choice()
        rps_result = rps(playerChoice, cpus_choice)

        # get text from eventText() in rps.py
        outputText = eventText(playerChoice, cpus_choice)

        # also update the scores here
        resultText = None
        if rps_result == 0:
            resultText = "\nIt's a tie!"
        if rps_result == 1:
            resultText = "\nYou win!"
            playerScore += 1
        if rps_result == 2:
            resultText = "\nThe CPU wins!"
            cpuScore += 1

        outputText = outputText + resultText

        self.label_events.setText(outputText)
        self.label_playerscore.setText(str(playerScore))
        self.label_cpuscore.setText(str(cpuScore))

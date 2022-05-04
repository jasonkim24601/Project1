from PyQt5.QtWidgets import *
from gui import Ui_MainWindow
from rps import *
import emoji

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

    def submit(self):
        playerChoice = 0
        playerChoiceText = 0

        global playerScore
        global cpuScore

        if self.rButton_rock.isChecked():
            playerChoice = 1
            playerChoiceText = "Rock"
        if self.rButton_paper.isChecked():
            playerChoice = 2
            playerChoiceText = "Paper"
        if self.rButton_scissors.isChecked():
            playerChoice = 3
            playerChoiceText = "Scissors"

        cpus_choice = cpu_choice()
        rps_result = rps(playerChoice, cpus_choice)

        if cpus_choice == 1:
            cpuChoiceText = "Rock"
        if cpus_choice == 2:
            cpuChoiceText = "Paper"
        if cpus_choice == 3:
            cpuChoiceText = "Scissors"

        # convert choices to text and then output each player's choice
        outputText = "You chose %s, the computer chose %s" % (playerChoiceText, cpuChoiceText)

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

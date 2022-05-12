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

        # Start by hiding all the images and win text
        self.label_cpu_rock.hide()
        self.label_cpu_paper.hide()
        self.label_cpu_scissor.hide()
        self.label_player_rock.hide()
        self.label_player_paper.hide()
        self.label_player_scissor.hide()

        self.label_winner.hide()

    def submit(self):
        """
        Method to handle actions once Go! button is pushed.
        Pulls value from selected radio button and uses rps() from rps.py to process it.
        Then it uses eventText() from rps.py to convert the results into text.
        After that it appends the text received by tacking on the winning player announcement, updates the score and displays the proper image for each player.
        """
        # Make sure one of the radio buttons is checked before doing anything
        if self.rButton_rock.isChecked() or self.rButton_paper.isChecked() or self.rButton_scissors.isChecked():
            self.label_cpu_rock.hide()
            self.label_cpu_paper.hide()
            self.label_cpu_scissor.hide()
            self.label_player_rock.hide()
            self.label_player_paper.hide()
            self.label_player_scissor.hide()

            playerChoice = None

            global playerScore
            global cpuScore
            # Grab value from radio buttons to determine human player's choice
            # Also show the correct corresponding image.
            if self.rButton_rock.isChecked():
                playerChoice = 1
                self.label_player_rock.show()
            if self.rButton_paper.isChecked():
                playerChoice = 2
                self.label_player_paper.show()
            if self.rButton_scissors.isChecked():
                playerChoice = 3
                self.label_player_scissor.show()
            # generate cpu's choice and show the corresponding image.
            cpus_choice = cpu_choice()
            if cpus_choice == 1:
                self.label_cpu_rock.show()
            if cpus_choice == 2:
                self.label_cpu_paper.show()
            if cpus_choice == 3:
                self.label_cpu_scissor.show()

            # process who won
            rps_result = rps(playerChoice, cpus_choice)

            # get text from eventText() in rps.py
            outputText = eventText(playerChoice, cpus_choice)

            # update the scores and append outputText to reflect it
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
            # change labels on GUI
            self.label_events.setText(outputText)
            self.label_playerscore.setText(str(playerScore))
            self.label_cpuscore.setText(str(cpuScore))

            # if someone made it to 5 points...
            if playerScore == 5:
                self.rButton_rock.hide()
                self.rButton_paper.hide()
                self.rButton_scissors.hide()
                self.pButton_submit.hide()
                self.label_winner.setText("YOU WIN!!!")
                self.label_winner.show()
            if cpuScore == 5:
                self.rButton_rock.hide()
                self.rButton_paper.hide()
                self.rButton_scissors.hide()
                self.pButton_submit.hide()
                self.label_winner.setText("YOU LOSE...")
                self.label_winner.show()
        else:
            self.label_events.setText('Please select an option!')

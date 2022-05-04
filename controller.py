from PyQt5.QtWidgets import *
from gui import Ui_MainWindow


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.pButton_submit.clicked.connect(lambda : self.submit())

    def submit(self):
        self.label_events.setText("It works!")

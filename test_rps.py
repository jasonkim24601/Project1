import pytest
from rps import *


def test_cpu_choice():
    """
    Testing cpu_choice by generating a few results and seeing that it falls in the correct range.
    """
    i = 0
    while i != 100:
        test_choice = cpu_choice()
        assert 1 <= test_choice <= 3
        i += 1


def test_rps():
    """
    Testing to ensure proper outcome is determined based on player and cpu choice.
    See documentation in rps.py's rps() for details.
    """
    assert rps(1, 1) == 0
    assert rps(1, 2) == 2
    assert rps(1, 3) == 1

    assert rps(2, 1) == 1
    assert rps(2, 2) == 0
    assert rps(2, 3) == 2

    assert rps(3, 1) == 2
    assert rps(3, 2) == 1
    assert rps(3, 3) == 0


def test_eventText():
    """
    Testing to make sure proper strings are created from eventText()
    """
    assert eventText(1, 1).__str__() == "You chose Rock, the computer chose Rock"
    assert eventText(1, 2).__str__() == "You chose Rock, the computer chose Paper"
    assert eventText(1, 3).__str__() == "You chose Rock, the computer chose Scissors"

    assert eventText(2, 1).__str__() == "You chose Paper, the computer chose Rock"
    assert eventText(2, 2).__str__() == "You chose Paper, the computer chose Paper"
    assert eventText(2, 3).__str__() == "You chose Paper, the computer chose Scissors"

    assert eventText(3, 1).__str__() == "You chose Scissors, the computer chose Rock"
    assert eventText(3, 2).__str__() == "You chose Scissors, the computer chose Paper"
    assert eventText(3, 3).__str__() == "You chose Scissors, the computer chose Scissors"

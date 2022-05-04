import random

def cpu_choice():
    """
    This function exists to randomly choose the CPU's choice.
    The return value here will be used for printing out the computer's choice on the GUI and to
        battle against the player's choice.
    :return: 1 if rock, 2 if paper, 3 if scissors
    """

    return random.randint(1, 3)

def rps(user_input, cpu_input):
    """
    This function will grab the user input, generate a random CPU choice and see who wins or if a draw occurs.
    :param user_input: Input grabbed from the selected radio button on the GUI:
    :param cpu_input: Input passed from cpu_choice.
    :return: 0 if draw, 1 if player win, 2 if CPU win
    """
    # 1 is rock
    # 2 is paper
    # 3 is scissors


    # first check for a draw
    if user_input == cpu_input:
        return 0

    # if the player chose rock
    if user_input == 1:
        # cpu chose paper
        if cpu_input == 2:
            return 2
        else:
            return 1
    # if the player chose paper
    if user_input == 2:
        # cpu chose rock
        if cpu_input == 1:
            return 1
        else:
            return 2
    # if the player chose scissors
    if user_input == 3:
        # cpu chose rock
        if cpu_input == 1:
            return 2
        else:
            return 1

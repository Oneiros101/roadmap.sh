MAIN_MENU = """
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
A number of chances will be defined based on your difficulty choice.
"""

LEVEL_CHOICE = """
Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
"""


def display_main_menu():
    print(MAIN_MENU)


def display_level_prompt():
    print(LEVEL_CHOICE)

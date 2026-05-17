import math
import random
import os
import time

from enum import Enum
from prompt import (display_main_menu,
                    display_level_prompt)


class Difficulty(Enum):
    EASY = 10
    MEDIUM = 5
    HARD = 3


def clean_screen():
    os.system("cls" if os.name == "nt" else "clear")


def choose_difficulty():
    wrong_input = True
    choice = input("Enter your choice (1, 2, 3 or 'quit' to quit the game): ")

    while wrong_input:
        if choice == "quit":
            print("\nQuitting game...\n")
            exit()
        else:
            if not choice.isdigit() or int(choice) > 3:
                choice = input("Wrong input. Enter your choice (1, 2, 3 or 'quit' to quit the game): ")
            else:
                if int(choice) == 1:
                    return Difficulty.EASY.value
                elif int(choice) == 2:
                    return Difficulty.MEDIUM.value
                elif int(choice) == 3:
                    return Difficulty.HARD.value


def play_game():
    start_time = time.perf_counter()
    random_number = random.randint(1, 100)
    guess = ""
    attempts = 0
    number_of_chances = choose_difficulty()

    print(f"Great! You have selected the {Difficulty(number_of_chances).name} difficulty level.")
    print("Let's start the game!\n")

    while guess != "quit":
        if attempts != number_of_chances:
            guess = input("Enter your guess (or 'quit' to quit the game): ")
            attempts += 1

            if guess == "quit":
                print("\nQuitting game...\n")
            else:
                if int(guess) > random_number:
                    print(f"Incorrect! The number is less than {guess}.\n")
                if int(guess) < random_number:
                    print(f"Incorrect! The number is greater than {guess}.\n")
                if int(guess) == random_number:
                    print(f"\nCongratulations! You guessed the correct number in {attempts} attempts.")
                    end_time = time.perf_counter()
                    total_time = end_time - start_time
                    print(f"You have completed the game in {math.ceil(total_time)} seconds.\n")
                    return
        else:
            print("GAME OVER! You have exceeded the number of chances.")
            end_time = time.perf_counter()
            total_time = end_time - start_time
            print(f"Total gameplay: {math.ceil(total_time)} seconds\n")

            return


def main():
    clean_screen()
    display_main_menu()
    display_level_prompt()
    play_game()


if __name__ == "__main__":
    main()


# Number Guessing Game

## Overview
This is a simple command-line-based Number Guessing Game written in Python. The objective is to guess a randomly generated number between 1 and 100 within a set number of chances based on the chosen difficulty level. The game features multiple difficulty levels and tracks the time taken to complete the game.

## Features
- Three levels of difficulty: Easy, Medium, and Hard.
- Randomly generates a number between 1 and 100.
- Tracks the number of attempts and time taken to guess the number.
- Option to quit the game at any time by entering "quit".

## Game Structure
- `guess.py`: This file contains the main game logic, including the functions for choosing difficulty, playing the game, and managing user inputs.
- `prompt.py`: This file defines the main menu and difficulty level prompt that is displayed to the user.

## How to Play
1. Run the `guess.py` file.
   ```bash
   python guess.py
   ```
2. Choose your desired difficulty level:
   - **Easy**: 10 chances
   - **Medium**: 5 chances
   - **Hard**: 3 chances
3. Enter your guess. The game will provide feedback on whether your guess is too high or too low.
4. Continue guessing until you either guess the correct number or run out of chances.
5. You can quit the game anytime by typing `quit`.

## Requirements
- Python 3.x

## Running the Game
To start the game, execute the following command:

```bash
python guess.py
```

Make sure to have the `prompt.py` file in the same directory as `guess.py`.

## Example
```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
A number of chances will be defined based on your difficulty choice.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

Enter your choice (1, 2, 3 or 'quit' to quit the game): 2
Great! You have selected the MEDIUM difficulty level.
Let's start the game!

Enter your guess: 50
Incorrect! The number is less than 50.

Enter your guess: 25
Incorrect! The number is greater than 25.

...

Congratulations! You guessed the correct number in 4 attempts.
You have completed the game in 30 seconds.
```

## Project URL:
https://roadmap.sh/projects/number-guessing-game
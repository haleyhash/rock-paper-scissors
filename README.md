# Rock, Paper, Scissors Game

This Python program simulates a game of Rock, Paper, Scissors between two players, reporting the scores of each player after each round.

## Overview

The game consists of the following components:

- **Players:** There are several types of players, including:
  - **HumanPlayer:** A player that prompts the user to choose a move (rock, paper, or scissors).
  - **RandomPlayer:** A player that randomly selects a move.
  - **ReflectPlayer:** A player that copies the opponent's last move.
  - **CyclePlayer:** A player that cycles through moves (rock, paper, scissors).
  - **RockPlayer:** A player that always chooses rock.

- **Gameplay:** The game proceeds through a series of rounds. Each round, both players select a move, and the outcome of the round is determined based on the moves chosen by the players.
- **Scoring:** Points are assigned to each player based on the outcome of the round. The player with the highest score at the end of the game is declared the winner.

## How to Play

1. **Run the Program:** Execute the Python script in your local environment.
2. **Follow On-Screen Instructions:** The program will prompt you to select your move (rock, paper, or scissors) for each round.
3. **View Results:** After each round, the program will display the moves chosen by both players and the current score.
4. **Game Over:** The game ends after a specified number of rounds, and the final scores are displayed along with the winner.

## Technologies Used

- Python 3

## Usage

To play the Rock, Paper, Scissors game, simply run the Python script in your terminal or preferred Python environment.

```bash
python rock_paper_scissors.py
```

## Acknowledgements
This project was created by Haley Hash. Special thanks to the inspiration and guidance from Udacity.

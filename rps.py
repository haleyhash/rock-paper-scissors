#!/usr/bin/env python3

import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    my_move = None
    their_move = None
    index_of_current_move = 0

    def move(self):  # this class of player always chooses rock
        return 'rock'

    def learn(self, my_move, their_move):  # method signature
        pass


class RandomPlayer(Player):
    def move(self):  # player chooses move at random
        return random.choice(moves)


class RockPlayer(Player):
    def move(self):  # player always chooses rock
        return 'rock'


class ReflectPlayer(Player):
    def move(self):  # copies opponent's last move
        if self.my_move is None:
            return random.choice(moves)
        else:
            return self.their_move

    def learn(self, my_move, their_move):  # stores the value of 'their_move'
        self.their_move = their_move


class CyclePlayer(Player):
    def move(self):  # player cycles through moves
        next_move = moves[self.index_of_current_move]
        self.index_of_current_move = \
            (self.index_of_current_move + 1) % len(moves)
        return next_move

    def learn(self, my_move, their_move):  # stores the value of 'my_move'
        self.my_move = my_move


class HumanPlayer(Player):
    def move(self):  # asks human to pick move
        self.my_move = input("\nRock, paper, or scissors?\n").lower()
        while True:
            if "rock" in self.my_move:
                return ("rock")
            elif "paper" in self.my_move:
                return ("paper")
            elif "scissors" in self.my_move:
                return ("scissors")
            else:
                print("\nI don't understand, try again")
                self.my_move = input(
                    "Rock, paper, or scissors?\n").lower()


def beats(one, two):  # assigns points to moves
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):  # defines player and sets score at 0
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):  # gets players' moves and prints them
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1} Player 2: {move2}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        # outcome of round
        if move1 == move2:
            print("It's a tie!")
        elif beats(move1, move2):
            self.p1_score += 1
            print("Player 1 wins this round!")
        else:
            self.p2_score += 1
            print("Player 2 won!")
        print(f"\nScore: Player one score: {self.p1_score}, "
              f"Player two score: {self.p2_score}\n")

    def play_game(self):
        print("\nGame start!\n")
        self.rounds = 3
        for round in range(self.rounds):
            print(f"Round {round}:")
            self.play_round()
        # display final score
        print(f"\nScore: Player one FINAL SCORE: {self.p1_score}, "
              f"Player two FINAL SCORE: {self.p2_score}\n")
        # announce winner
        if self.p1_score > self.p2_score:
            print("Player One is the champion!")
        elif self.p1_score < self.p2_score:
            print("Player Two is the champion!")
        else:
            print("It is a tie!")
        print("\nGame over!\n")


if __name__ == '__main__':
    # human player vs random computer player type
    game = Game(HumanPlayer(), random.choice(
        [RandomPlayer(), ReflectPlayer(), CyclePlayer()]))
    game.play_game()

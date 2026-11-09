"""Terminal front end: a two-player game loop on top of the Board rules."""

import random

from gridlock.board import MARKS, Board

PROMPT = "Player {player} ({mark}) - enter row and column (0-2): "


def read_move(board, player, input_fn=input):
    """Ask until the player enters a legal move, then place it on the board."""
    mark = MARKS[player - 1]
    while True:
        raw = input_fn(PROMPT.format(player=player, mark=mark))
        try:
            row, col = (int(part) for part in raw.split())
        except ValueError:
            print("Enter two whole numbers separated by a space, for example: 1 2")
            continue
        try:
            board.place(row, col, mark)
        except ValueError as error:
            print(error)
            continue
        return


def play(input_fn=input, rng=random):
    """Play one game. Returns the winning player number (1 or 2), or None for a tie."""
    board = Board()
    player = rng.choice((1, 2))  # either player may open
    print(f"Player {player} goes first.\n")
    print(board.render(), end="\n\n")
    while True:
        read_move(board, player, input_fn)
        print(board.render(), end="\n\n")
        if board.winner():
            print(f"Player {player} wins!")
            return player
        if board.is_full():
            print("It's a tie.")
            return None
        player = 2 if player == 1 else 1


def session(input_fn=input, rng=random):
    """Play games until the players decline a rematch. Returns the tally of results."""
    tally = {1: 0, 2: 0, "ties": 0}
    while True:
        winner = play(input_fn, rng)
        tally[winner or "ties"] += 1
        print(f"Score - Player 1: {tally[1]}, Player 2: {tally[2]}, ties: {tally['ties']}\n")
        if input_fn("Play again? (y/n): ").strip().lower() not in ("y", "yes"):
            return tally


def main():
    try:
        session()
    except (EOFError, KeyboardInterrupt):
        print("\nGame aborted.")

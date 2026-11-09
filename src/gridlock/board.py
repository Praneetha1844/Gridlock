"""Tic-tac-toe rules: board state, move validation and win detection (no I/O)."""

SIZE = 3
EMPTY = "-"
MARKS = ("X", "O")  # player 1 plays X, player 2 plays O

# Every winning line as a tuple of (row, col): rows, columns, then both diagonals.
LINES = (
    *(tuple((r, c) for c in range(SIZE)) for r in range(SIZE)),
    *(tuple((r, c) for r in range(SIZE)) for c in range(SIZE)),
    tuple((i, i) for i in range(SIZE)),
    tuple((i, SIZE - 1 - i) for i in range(SIZE)),
)


class Board:
    def __init__(self):
        self.cells = [[EMPTY] * SIZE for _ in range(SIZE)]

    def place(self, row, col, mark):
        """Put mark on (row, col). Raises ValueError for an off-board or occupied cell."""
        if not (0 <= row < SIZE and 0 <= col < SIZE):
            raise ValueError(f"Row and column must be between 0 and {SIZE - 1}.")
        if self.cells[row][col] != EMPTY:
            raise ValueError("That cell is already taken.")
        self.cells[row][col] = mark

    def winner(self):
        """Return the winning mark, or None if nobody has won yet."""
        for line in LINES:
            marks = {self.cells[r][c] for r, c in line}
            if len(marks) == 1 and EMPTY not in marks:
                return marks.pop()
        return None

    def is_full(self):
        return all(cell != EMPTY for row in self.cells for cell in row)

    def render(self):
        return "\n".join(" ".join(row) for row in self.cells)

import pytest

from gridlock.board import EMPTY, LINES, SIZE, Board


def test_new_board_is_empty_with_no_winner():
    board = Board()
    assert board.winner() is None
    assert not board.is_full()
    assert board.render() == "- - -\n- - -\n- - -"


@pytest.mark.parametrize("line", LINES)
def test_every_line_wins(line):
    board = Board()
    for row, col in line:
        board.place(row, col, "O")
    assert board.winner() == "O"


def test_there_are_eight_lines():
    assert len(LINES) == 2 * SIZE + 2


def test_mixed_line_is_not_a_win():
    board = Board()
    board.place(0, 0, "X")
    board.place(0, 1, "O")
    board.place(0, 2, "X")
    assert board.winner() is None


def test_occupied_cell_is_rejected_and_unchanged():
    board = Board()
    board.place(1, 1, "X")
    with pytest.raises(ValueError, match="already taken"):
        board.place(1, 1, "O")
    assert board.cells[1][1] == "X"


@pytest.mark.parametrize("row, col", [(-1, 0), (0, -1), (3, 0), (0, 3)])
def test_off_board_cell_is_rejected(row, col):
    with pytest.raises(ValueError, match="between 0 and 2"):
        Board().place(row, col, "X")


def test_full_board_without_a_winner():
    board = Board()
    layout = ["XOX", "XXO", "OXO"]
    for r, row in enumerate(layout):
        for c, mark in enumerate(row):
            board.place(r, c, mark)
    assert board.is_full()
    assert board.winner() is None
    assert all(cell != EMPTY for row in board.cells for cell in row)

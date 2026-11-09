from gridlock.game import play, session


class FirstOption:
    """Stand-in for random: always lets player 1 open."""

    def choice(self, options):
        return options[0]


def scripted(inputs):
    remaining = iter(inputs)
    return lambda prompt: next(remaining)


def test_player_one_wins_top_row(capsys):
    moves = ["0 0", "1 0", "0 1", "1 1", "0 2"]
    assert play(scripted(moves), FirstOption()) == 1
    assert "Player 1 wins!" in capsys.readouterr().out


def test_player_two_can_win(capsys):
    moves = ["0 0", "1 0", "0 1", "1 1", "2 2", "1 2"]
    assert play(scripted(moves), FirstOption()) == 2
    assert "Player 2 wins!" in capsys.readouterr().out


def test_full_board_is_a_tie(capsys):
    moves = ["0 0", "0 1", "0 2", "1 2", "1 0", "2 0", "1 1", "2 2", "2 1"]
    assert play(scripted(moves), FirstOption()) is None
    assert "It's a tie." in capsys.readouterr().out


def test_bad_input_is_reported_and_retried(capsys):
    moves = ["x", "3 3", "1", "0 0", "0 0", "1 1", "0 1", "2 2", "0 2"]
    assert play(scripted(moves), FirstOption()) == 1
    out = capsys.readouterr().out
    assert "Enter two whole numbers" in out
    assert "between 0 and 2" in out
    assert "already taken" in out

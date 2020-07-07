from game import who_wins, is_input_valid

import pytest


def test_is_input_valid_return_false_if_given_string_that_is_not_in_the_given_list():
    options = ["hello", "hola", "ola"]
    assert is_input_valid("an invalid string", options) == False


def test_is_input_valid_return_true_if_given_string_that_is_in_the_given_list():
    options = ["hello", "hola", "ola"]
    assert is_input_valid("hola", options) == True


def test_who_wins_returns_draw_if_both_players_play_the_same():
    assert who_wins(player="paper", bot="paper") == "its a draw"


def test_who_wins_returns_player_wins_if_player_gives_paper_and_bot_gives_rock():
    assert who_wins(player="paper", bot="rock") == "player wins"


def test_who_wins_returns_bot_wins_if_player_gives_paper_and_bot_gives_scissors():
    assert who_wins(player="paper", bot="scissors") == "bot wins"


def test_who_wins_returns_player_wins_if_player_gives_rock_and_bot_gives_scissors():
    assert who_wins(player="rock", bot="scissors") == "player wins"


def test_who_wins_returns_bot_wins_if_player_gives_rock_and_bot_gives_paper():
    assert who_wins(player="rock", bot="paper") == "bot wins"


def test_who_wins_returns_player_wins_if_player_gives_scissors_and_bot_gives_paper():
    assert who_wins(player="scissors", bot="paper") == "player wins"


def test_who_wins_returns_bot_wins_if_player_gives_scissors_and_bot_gives_rock():
    assert who_wins(player="scissors", bot="rock") == "bot wins"

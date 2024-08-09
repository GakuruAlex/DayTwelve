import pytest
from unittest.mock import patch
from number_guessing_game import number_generator, number_guessing_game, play_game

class TestNumberGenerator:
    @pytest.mark.xfail(reason="This test is meant to fail")
    def test_number_generator_range_goes_to_100(self):
        for _ in range(1000):
            result = number_generator()
            assert result >= 1 and result <= 99

class TestNumberGuessingGame:
    @pytest.mark.parametrize("guess, number, result", [
        (2, 2, ("You got it right. The number was 2", True)),
        (73, 73, (f"You got it right. The number was 73", True)),
        (33, 33, (f"You got it right. The number was 33", True)),
        (50, 50, (f"You got it right. The number was 50", True))
    ])
    def test_number_guessing_game_with_correct_guess(self, guess, number, result):
        assert number_guessing_game(number, guess) == result
    
    @pytest.mark.parametrize("guess, number, result", [
        (50, 70, ("Too low!", False)),
        (60, 70, ("Too low!", False)),
        (65, 70, ("Too low!", False)),
        (69, 70, ("Too low!", False))
    ])
    def test_number_guessing_game_with_guess_too_low(self, number, guess, result):
        assert number_guessing_game(number, guess) == result
    @pytest.mark.parametrize("number, guess, result", [
        (30, 50, ("Too high", False)),
        (30, 45, ("Too high", False)),
        (30, 40, ("Too high", False)),
        (30, 35, ("Too high", False))
    ])
    def test_number_generator_with_guess_too_high(self, number, guess, result):
        assert number_guessing_game(number, guess) == result
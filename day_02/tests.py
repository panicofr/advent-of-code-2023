import unittest

from puzzle import Bag, Game, parse_game_line, Round


class TestCase(unittest.TestCase):
    def test_parse_game(self) -> None:
        game_line: str = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        game: Game = parse_game_line(game_line)

        self.assertEqual(game.id, 1)
        self.assertEqual(len(game.rounds), 3)
        self.assertEqual(game.rounds[0].blue, 3)
        self.assertEqual(game.rounds[0].red, 4)
        self.assertEqual(game.rounds[0].green, 0)

    def test_is_round_valid(self):
        round = Round(red=5, blue=8, green=6)
        bag = Bag(red=12, blue=10, green=9)
        self.assertTrue(round.is_valid(bag))

    
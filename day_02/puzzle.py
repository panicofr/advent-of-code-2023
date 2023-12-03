from __future__ import annotations

from dataclasses import dataclass, field
import re
import sys


@dataclass
class Bag:
    blue: int = field(kw_only=True)
    red: int = field(kw_only=True)
    green: int = field(kw_only=True)


@dataclass
class Round:
    blue: int = field(default=0)
    red: int = field(default=0)
    green: int = field(default=0)

    def is_valid(self, bag: Bag):
        return all([self.blue <= bag.blue, self.red <= bag.red, self.green <= bag.green])


@dataclass
class Game:
    id: int = field(default=0)
    rounds: list[Round] = field(default_factory=list)

    @property
    def power(self):
        red = max(r.red for r in self.rounds)
        blue = max(r.blue for r in self.rounds)
        green = max(r.green for r in self.rounds)
        return red * blue * green

def parse_game_line(line: str) -> Game:
    game = Game()
    game.rounds.append(Round())
    next_word = None
    next_value = None

    for token in line.split():
        if token == "Game":
            next_word = "identifier"

        elif token.endswith(":"):
            game.id = int(token[:-1])

        elif token.endswith(","):
            color = token[:-1]
            setattr(game.rounds[-1], color, next_value)

        elif token.endswith(";"):
            color = token[:-1]
            setattr(game.rounds[-1], color, next_value)
            game.rounds.append(Round())

        elif token.isdigit():
            next_value = int(token)

        elif token in ("red", "green", "blue"):
            setattr(game.rounds[-1], token, next_value)

        else:
            raise Exception(f"Unexpected token: {token}")

    return game

def part1():
    bag = Bag(red=12, green=13, blue=14)
    games = [parse_game_line(l) for l in open("input.txt").readlines()]
    valid_games = [g for g in games if all(r.is_valid(bag) for r in g.rounds)]
    print(sum(g.id for g in valid_games))

def part2():
    games = [parse_game_line(l) for l in open("input.txt").readlines()]
    print(sum([g.power for g in games]))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '1':
        part1()
    if len(sys.argv) > 1 and sys.argv[1] == '2':
        part2()
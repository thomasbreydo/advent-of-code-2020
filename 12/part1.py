from typing import Iterator, Tuple, List
from enum import Enum

INPUT: str = "input.txt"


def gen_input(file: str) -> Iterator[Tuple[str, int]]:
    with open(file) as f:
        return ((line[0], int(line[1:])) for line in f.read().split("\n"))


class Direction(Enum):
    EAST = (1, 0)
    SOUTH = (0, -1)
    WEST = (-1, 0)
    NORTH = (0, 1)

    @classmethod
    def fromstring(cls, string: str):
        first_letter = string[0].lower()
        if first_letter == "e":
            return cls.EAST
        if first_letter == "w":
            return cls.WEST
        if first_letter == "n":
            return cls.NORTH
        if first_letter == "s":
            return cls.SOUTH
        raise ValueError("invalid direction")


class Ship:
    x: int
    y: int
    facing: Direction
    _CLOCKWISE_DIRECTIONS: List[Direction] = [
        Direction.EAST,
        Direction.SOUTH,
        Direction.WEST,
        Direction.NORTH,
    ]
    _N_DIRECTIONS: int = len(_CLOCKWISE_DIRECTIONS)

    def __init__(self, x: int, y: int, facing: Direction = Direction.EAST):
        self.x = x
        self.y = y
        self.facing = facing

    def move(self, action: str, value: int):
        action = action.upper()
        if action == "F":
            self.move_in_direction(self.facing, value)
        elif action in ("L", "R"):
            if action == "L":
                value *= -1
            self.turn_right(value)
        elif action in ("N", "S", "W", "E"):
            self.move_in_direction(Direction.fromstring(action), value)

    def move_in_direction(self, direction: Direction, value: int):
        left_right_coef, up_down_coef = direction.value
        self.x += left_right_coef * value
        self.y += up_down_coef * value

    def manhattan_distance_to(self, x: int, y: int) -> int:
        """Calculate the Manhattan distance between this ship and (`x`, `y`)."""
        return abs(self.x - x) + abs(self.y - y)

    def turn_right(self, degrees: int):
        index: int = self._CLOCKWISE_DIRECTIONS.index(self.facing)
        self.facing = self._CLOCKWISE_DIRECTIONS[
            (index + (degrees // 90)) % self._N_DIRECTIONS
        ]


def main():
    action: str
    value: int
    start_location: Tuple[int, int] = (0, 0)
    ship: Ship = Ship(*start_location)
    for action, value in gen_input(INPUT):
        ship.move(action, value)
    print(ship.manhattan_distance_to(*start_location))


if __name__ == "__main__":
    main()

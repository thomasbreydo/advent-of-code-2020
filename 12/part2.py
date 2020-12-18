from typing import Union, Tuple, Any
from part1 import Direction, gen_input

INPUT = "input.txt"


Location = Tuple[int, int]


class Ship:
    location: Location
    relative_waypoint: Location

    def __init__(
        self,
        location: Union[Location, None] = None,
        relative_waypoint: Union[Location, None] = None,
    ):
        if location is None:
            location = (0, 0)
        if relative_waypoint is None:
            relative_waypoint = (10, 1)
        self.location = location
        self.relative_waypoint = relative_waypoint

    def move(self, action: str, value: int):
        action = action.upper()
        if action == "F":
            self.forward(value)
        elif action in ("L", "R"):
            if action == "L":
                value *= -1
            self.rotate_clockwise(value)
        elif action in ("N", "S", "W", "E"):
            self.move_waypoint(Direction.fromstring(action), value)

    def forward(self, value: int):
        left_right_coef, up_down_coef = self.relative_waypoint
        new_x: int = self.location[0] + left_right_coef * value
        new_y: int = self.location[1] + up_down_coef * value
        self.location = new_x, new_y

    def move_waypoint(self, direction: Direction, value: int):
        left_right_coef, up_down_coef = direction.value
        a, b = self.relative_waypoint
        self.relative_waypoint = a + left_right_coef * value, b + up_down_coef * value

    def rotate_clockwise(self, degrees: int):
        a, b = self.relative_waypoint
        rotation = (degrees // 90) % 4
        if rotation == 1:
            self.relative_waypoint = b, -a
        elif rotation == 2:
            self.relative_waypoint = -a, -b
        elif rotation == 3:
            self.relative_waypoint = -b, a

    def manhattan_distance_to(self, x: int, y: int) -> int:
        """Calculate the Manhattan distance between this ship and (`x`, `y`)."""
        return abs(self.location[0] - x) + abs(self.location[1] - y)


def main():
    action: str
    value: int
    start_location: Tuple[int, int] = (0, 0)
    relative_waypoint: Location = (10, 1)
    ship: Ship = Ship(start_location, relative_waypoint)
    for action, value in gen_input(INPUT):
        ship.move(action, value)
    print(ship.manhattan_distance_to(*start_location))


if __name__ == "__main__":
    main()

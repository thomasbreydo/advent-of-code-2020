from typing import List
import time
from part1 import Seats
from part1 import NoSeatsChanged

INPUT = "input.txt"


class Slope:
    def __init__(self, dy: int, dx: int):
        self.dx: int = dx
        self.dy: int = dy


class Seats2(Seats):

    SLOPES: List[Slope] = [
        Slope(x, y)
        for x, y in [
            (0, 1),
            (0, -1),
            (1, 0),
            (1, 1),
            (1, -1),
            (-1, 0),
            (-1, 1),
            (-1, -1),
        ]
    ]

    def __init__(self, rows):
        super().__init__(rows)

    def next_round_value_at(self: "Seats2", row_ind: int, col_ind: int) -> str:
        seat: str = self.current_value_at(row_ind, col_ind)
        if seat == ".":  # floor seats never get occupied
            return "."
        n_neighbors_visible: int = self.get_n_neighbors_visible_from(row_ind, col_ind)
        if seat == "L" and n_neighbors_visible == 0:
            return "#"
        if seat == "#" and n_neighbors_visible >= 5:
            return "L"
        return seat  # no change

    def get_n_neighbors_visible_from(self: "Seats2", row_ind: int, col_ind: int) -> int:
        return sum(
            self.exists_occupied_seat_visible_from(row_ind, col_ind, slope)
            for slope in self.SLOPES
        )

    def exists_occupied_seat_visible_from(
        self: "Seats2", row_ind: int, col_ind: int, slope: Slope
    ) -> int:
        while True:
            row_ind += slope.dy
            col_ind += slope.dx
            if self.is_out_of_bounds(row_ind, col_ind):
                break
            seat: str = self.current_value_at(row_ind, col_ind)
            if seat == "#":
                return True
            if seat == "L":
                return False
        return False

    def is_out_of_bounds(self: "Seats2", row_ind: int, col_ind: int) -> bool:
        return (
            (row_ind < 0)
            or (col_ind < 0)
            or (row_ind >= self.n_rows)
            or (col_ind >= self.n_cols)
        )


if __name__ == "__main__":
    seats: Seats2 = Seats2.fromfile(INPUT)
    start: float = time.time()
    while True:
        try:
            seats.next_round()
        except NoSeatsChanged:
            break
    print(seats.n_occupied)
    end: float = time.time()
    print(f"Found in {end - start} seconds.")

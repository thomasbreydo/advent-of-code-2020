from typing import List, Union, Type, Iterator, TextIO

INPUT = "input.txt"


class NoSeatsChanged(Exception):
    pass


class Seats:
    def __init__(self: "Seats", rows: List[str]) -> None:
        self.rows: List[str] = rows
        self.n_rows: int = len(rows)
        self.n_cols: int = len(rows[0])

    @classmethod
    def fromstring(cls: Type["Seats"], layout: str) -> "Seats":
        return cls(layout.split("\n"))

    @classmethod
    def fromfile(cls: Type["Seats"], filename: str) -> "Seats":
        with open(filename) as f:
            return cls.fromstring(f.read())

    def __str__(self):
        return "\n".join(self.rows)

    def next_round(self: "Seats") -> None:
        new_rows: List[str] = [
            "".join(self.next_round_value_at(i, j) for j in range(self.n_cols))
            for i in range(self.n_rows)
        ]
        if new_rows == self.rows:
            raise NoSeatsChanged("no seats changed")
        self.rows = new_rows

    def next_round_value_at(self: "Seats", row_ind: int, col_ind: int) -> str:
        seat: str = self.current_value_at(row_ind, col_ind)
        if seat == ".":  # floor seats never get occupied
            return "."
        n_occupied_neighbors: int = self.get_n_occupied_neighbors_at(row_ind, col_ind)
        if seat == "L" and n_occupied_neighbors == 0:
            return "#"
        if seat == "#" and n_occupied_neighbors >= 4:
            return "L"
        return seat  # no change

    def current_value_at(self: "Seats", row_ind: int, col_ind: int) -> str:
        return self.rows[row_ind][col_ind]

    def get_n_occupied_neighbors_at(self: "Seats", row_ind: int, col_ind: int) -> int:
        return sum(neighbor == "#" for neighbor in self.get_neighbors(row_ind, col_ind))

    def get_neighbors(self: "Seats", row_ind: int, col_ind: int) -> Iterator[str]:
        lower_bound_row: int = max(row_ind - 1, 0)  # -1 isn't adjacent to top-row seats
        lower_bound_col: int = max(col_ind - 1, 0)  # -1 isn't adjacent to left-col seats
        i: int
        for i in range(lower_bound_row, row_ind + 2):
            j: int
            for j in range(lower_bound_col, col_ind + 2):
                if i == row_ind and j == col_ind:
                    continue  # the seat isn't adjacent to itself
                try:
                    yield self.rows[i][j]
                except IndexError:  # skip out-of-bounds neighbors for bottom-row and right-col seats
                    continue

    @property
    def n_occupied(self):
        return sum(row.count("#") for row in self.rows)


if __name__ == "__main__":
    seats: Seats = Seats.fromfile(INPUT)
    while True:
        try:
            seats.next_round()
        except NoSeatsChanged:
            break
    print(seats.n_occupied)

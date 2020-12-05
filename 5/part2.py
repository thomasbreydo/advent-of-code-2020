from typing import Iterable
from part1 import get_id

INPUT = "input.txt"


class BoardingPass:
    def __init__(self, row: int, col: int):
        self.row: int = row
        self.col: int = col

    def __lt__(self, other: object) -> bool:
        if isinstance(other, BoardingPass):
            return self.id < other.id
        return NotImplemented

    def __str__(self) -> str:
        row: str = f"{self.row:07b}".replace("0", "F").replace("1", "B")
        col: str = f"{self.col:03b}".replace("0", "L").replace("1", "R")
        return row + col

    @classmethod
    def from_str(cls, string: str) -> object:
        return cls(*BoardingPass.str_to_row_col(string))

    @staticmethod
    def str_to_row_col(boarding_pass_str: str) -> (int, int):
        row: int = int(boarding_pass_str[:7].replace("F", "0").replace("B", "1"), 2)
        col: int = int(boarding_pass_str[7:].replace("L", "0").replace("R", "1"), 2)
        return row, col

    @property
    def id(self) -> int:
        return self.row * 8 + self.col


if __name__ == "__main__":
    with open(INPUT) as f:
        passes: Iterable = [
            BoardingPass.from_str(line) for line in f.read().split("\n")
        ]
        sorted_passes = sorted(passes)

    i: int
    boarding_pass: object
    for i, boarding_pass in enumerate(sorted_passes[1:]):
        prev_id: int = sorted_passes[
            i
        ].id  # i is offset by 1 bc enumerate takes sorted_passes[1:]
        cur_id: int = boarding_pass.id
        if prev_id + 1 != cur_id:
            print(cur_id - 1)

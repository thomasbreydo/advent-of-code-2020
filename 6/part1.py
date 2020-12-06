from typing import Iterable
from string import ascii_lowercase

INPUT: str = "input.txt"


def count(group):
    return sum(char in group for char in ascii_lowercase)


if __name__ == "__main__":
    with open(INPUT) as f:
        groups: Iterable[str] = f.read().split("\n\n")

    print(sum(count(group) for group in groups))

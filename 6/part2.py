from typing import Iterable
from string import ascii_lowercase

INPUT: str = "input.txt"


def count(group: str) -> int:
    return sum(
        all(char in person for person in group.split("\n")) for char in ascii_lowercase
    )


if __name__ == "__main__":
    with open(INPUT) as f:
        groups: Iterable[str] = f.read().split("\n\n")

    print(sum(count(group) for group in groups))

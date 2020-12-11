from collections import deque
from typing import Iterable

INPUT_FILE: str = "input.txt"


def two_sum_to_target(numbers: Iterable[int], target: int) -> bool:
    number: int
    for number in numbers:
        if target - number in numbers:
            if number != target / 2:  # the two addends must be different
                return True
    return False


def first_invalid(transmissions: Iterable[int], preamble_len: int = 25) -> int:
    previous: deque = deque(transmissions[:25], maxlen=preamble_len)
    for n in transmissions[25:]:
        if not two_sum_to_target(previous, n):
            return n
        previous.append(n)
    raise ValueError("no invalid transmissions")


if __name__ == "__main__":
    with open(INPUT_FILE) as f:
        print(first_invalid([int(x) for x in f.read().split("\n")]))

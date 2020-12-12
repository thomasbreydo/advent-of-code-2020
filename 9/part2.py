from typing import List

from part1 import first_invalid

INPUT_FILE: str = "input.txt"


def number_adding_to_first_invalid(transmissions: List[int]) -> List[int]:
    target: int
    target_i: int
    target_i, target = first_invalid(transmissions)
    i: int
    n: int
    for i, n in enumerate(transmissions[:target_i]):
        leftover: int = target - n
        solution: List[int] = [n]
        while leftover > 0:
            i += 1
            transmission: int = transmissions[i]
            leftover -= transmission
            solution.append(transmission)
            if leftover == 0:
                return solution


if __name__ == "__main__":
    with open(INPUT_FILE) as f:
        transmissions: List[int] = [int(x) for x in f.read().split("\n")]
    numbers: List[int] = number_adding_to_first_invalid(transmissions)
    print(min(numbers) + max(numbers))

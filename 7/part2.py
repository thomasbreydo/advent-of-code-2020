import time
from typing import Dict, Optional, List
from part1 import get_input_rules
import functools

INPUT: str = "input.txt"
TARGET: str = "shiny gold"


def cache(f_get_n_bags_inside):
    cache_map: Dict[str, int] = {}

    @functools.wraps(f_get_n_bags_inside)
    def new(color, rules):
        nonlocal cache_map

        try:
            return cache_map[color]
        except KeyError:
            cache_map[color]: int = f_get_n_bags_inside(color, rules)
            return cache_map[color]

    new.cache = cache_map
    new.cache_clear = cache_map.clear
    return new


@cache
def get_n_bags_inside(color: str, rules: Dict[str, Optional[List[str]]]) -> int:
    if not rules[color]:
        return 0
    n_bags: int = 0
    content_color: str
    quantity: str
    for quantity, content_color in rules[color]:
        count_per_bag: int = 1 + get_n_bags_inside(content_color, rules)
        n_bags += count_per_bag * int(quantity)
    return n_bags


if __name__ == "__main__":
    input_rules: Dict[str, Optional[List[str]]] = get_input_rules(INPUT)
    start = time.time()
    print(get_n_bags_inside(TARGET, input_rules))
    end = time.time()
    print(f"Recursion took {(end - start) * 1e3:f} ms")

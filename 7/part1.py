import functools
import re
import time
from typing import Pattern, Optional, Match, Dict, List, Any, Set

INPUT: str = "input.txt"
rule_re: Pattern[str] = re.compile(
    r"""
(?P<bag_type>\w+\s\w+) 
\sbags\scontain
(?P<bag_contains>
(\s\d+  # " 9"
\s\w+\s\w+  # " dark lavender"
\sbags?
[.,])+
)$
""",
    re.VERBOSE,
)
contains_no_bags_re: Pattern[str] = re.compile(
    r"^(?P<bag_type>\w+\s\w+)\sbags\scontain no other bags.$"
)
bag_contains_re: Pattern[str] = re.compile(
    r"""
(\d+)  # 2
\s
(\w+\s\w+)  # dark lavender
\s
bags?  # "bag" or "bags"
[.,]
""",
    re.VERBOSE,
)


def get_input_rules(input_file: str) -> object:
    rules: Dict[str, Optional[List[str]]] = {}
    with open(input_file) as f:
        line: str
        for line in f.read().split("\n"):
            rule_mo: Optional[Match[str]] = rule_re.match(line)
            try:
                bag_type: str = rule_mo.group("bag_type")
            except AttributeError:
                bag_type: str = contains_no_bags_re.match(line).group("bag_type")
                rules[bag_type] = []
            else:
                bag_contains: str = rule_mo.group("bag_contains")
                rules[bag_type] = bag_contains_re.findall(bag_contains)
    return rules


INPUT_RULES: Dict[str, Optional[List[str]]] = get_input_rules(INPUT)


@functools.lru_cache
def bag_a_contains_target_bag(bag_a: str, target_bag: str):
    what_bag_a_contains: Set[str] = {bag for _, bag in INPUT_RULES[bag_a]}
    if not what_bag_a_contains:
        return False
    if target_bag in what_bag_a_contains:
        return True
    for contained_bag in what_bag_a_contains:
        if bag_a_contains_target_bag(contained_bag, target_bag):
            return True
    return False


@functools.lru_cache
def get_n_containing_color(target_color: str):
    return sum(
        bag_a_contains_target_bag(color, target_color) for color in INPUT_RULES.keys()
    )


if __name__ == "__main__":
    start: float = time.time()
    print(get_n_containing_color("shiny gold"))
    end: float = time.time()
    print(f"Recursion took {(end - start) * 1e3:f} ms")

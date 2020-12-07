import re
from typing import Pattern, Optional, Match, Dict, List, Any

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


def get_input_rules() -> Dict[str, Optional[List[str]]]:
    rules: Dict[str, Optional[List[str]]] = {}
    with open(INPUT) as f:
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


def get_possible_contents(color, rules):
    possible_contents = set()
    for _, possible_content in rules[color]:
        possible_contents.add(possible_content)
        possible_contents.update(get_possible_contents(possible_content, rules))
    return possible_contents


def get_n_containing_color(target_color, rules):
    return sum(
        target_color in get_possible_contents(color, rules) for color in rules.keys()
    )


if __name__ == "__main__":
    input_rules = get_input_rules()
    print(get_n_containing_color("shiny gold", input_rules))

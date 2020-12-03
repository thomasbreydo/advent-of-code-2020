import math
import part1
import re


SLOPES_FILE = "part2_slopes.txt"
with open(SLOPES_FILE) as f:
    slopes = f.read()

if __name__ == "__main__":
    slope_regex = re.compile(r"Right (\d), down (\d)\.")
    print(
        math.prod(
            part1.get_n_trees_hit(part1.input_lines, int(right_steps), int(down_steps))
            for (right_steps, down_steps) in slope_regex.findall(slopes)
        )
    )

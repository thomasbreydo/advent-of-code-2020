INPUT = "input.txt"

with open(INPUT) as f:
    input_lines = f.readlines()


def get_n_trees_hit(lines, right_steps=3, down_steps=1):
    line_length = len(lines[0].strip())
    n_trees_hit = 0
    for i, line in enumerate(lines[::down_steps]):
        if line[(i * right_steps) % line_length] == "#":
            n_trees_hit += 1
    return n_trees_hit


if __name__ == "__main__":
    print(get_n_trees_hit(input_lines))

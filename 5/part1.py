INPUT = "input.txt"


def get_id(boarding_pass):
    row = int(boarding_pass[:7].replace("F", "0").replace("B", "1"), 2)
    col = int(boarding_pass[7:].replace("L", "0").replace("R", "1"), 2)
    return row * 8 + col


if __name__ == "__main__":
    with open(INPUT) as f:
        max_id = max(
            get_id(input_boarding_pass) for input_boarding_pass in f.read().split("\n")
        )
    print(max_id)

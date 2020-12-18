INPUT = "input.txt"


def main():
    with open(INPUT) as f:
        earliest, bus_notes = f.read().split("\n")
    earliest = int(earliest)
    ids = (int(id_) for id_ in bus_notes.split(",") if id_ != "x")
    id_, best_time_to_leave = min(
        [(id_, (earliest // id_ + 1) * id_) for id_ in ids], key=lambda tupl: tupl[1]
    )
    print(id_ * (best_time_to_leave - earliest))


if __name__ == "__main__":
    main()

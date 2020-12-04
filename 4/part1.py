INPUT = "input.txt"
FIELDS = "expected_fields_for_part_1.txt"


with open(FIELDS) as f:
    fields = f.read().split("\n")


def is_valid(passport):
    for field in fields:
        if field not in passport:
            return False
    return True


if __name__ == "__main__":
    with open(INPUT) as f:
        passports = f.read()
    print(sum(is_valid(passport) for passport in passports.split("\n\n")))

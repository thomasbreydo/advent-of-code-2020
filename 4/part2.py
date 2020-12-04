import re


INPUT = "input.txt"


fields_re = re.compile(r"([a-z]{3}):(\S+)\s?")
hgt_re = re.compile(r"^(?P<height>\d+)(?P<units>in|cm)$")
hcl_re = re.compile(r"^\#[0-9a-f]{6}$")
pid_re = re.compile(r"^[0-9]{9}$")


def is_valid(passport_str):
    fields = {key: value for key, value in fields_re.findall(passport_str)}
    try:
        return (
            valid_byr(fields["byr"])
            and valid_iyr(fields["iyr"])
            and valid_eyr(fields["eyr"])
            and valid_hgt(fields["hgt"])
            and valid_hcl(fields["hcl"])
            and valid_ecl(fields["ecl"])
            and valid_pid(fields["pid"])
        )
    except KeyError:  # missing field
        return False


def valid_byr(byr: str):
    return is_four_digits(byr) and in_range(byr, 1920, 2003)


def valid_iyr(iyr: str):
    return is_four_digits(iyr) and in_range(iyr, 2010, 2021)


def valid_eyr(eyr: str):
    return is_four_digits(eyr) and in_range(eyr, 2020, 2031)


def valid_hgt(hgt: str):
    if (height_mo := hgt_re.match(hgt)) is None:
        return False
    if height_mo.group("units") == "in":
        return in_range(height_mo.group("height"), 59, 77)
    return in_range(height_mo.group("height"), 150, 194)  # it's cm


def valid_hcl(hcl: str):
    return hcl_re.match(hcl) is not None


def valid_ecl(ecl: str):
    return ecl in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")


def valid_pid(pid: str):
    return pid_re.match(pid) is not None


def is_four_digits(value: str):
    return len(value) == 4


def in_range(value: str, lower: int, upper: int):
    return int(value) in range(lower, upper)


if __name__ == "__main__":
    with open(INPUT) as f:
        passports = f.read()
    print(sum(is_valid(passport) for passport in passports.split("\n\n")))

import re

INPUT = "input.txt"

with open(INPUT) as f:
    passwords = f.read()

regex = re.compile(
    r"""
(\d+)-(\d+)  # upper and lower bounds
\s
(\w):  # letter
\s
(\w+)  # password
""",
    re.VERBOSE,
)


def valid_password(lower, upper, letter, password):
    letter_count = 0
    for char in password:
        if char == letter:
            if letter_count == upper:
                return False
            letter_count += 1
    if letter_count >= lower:
        return True
    return False


n_valid_passwords = sum(
    valid_password(int(lower), int(upper), letter, password)
    for lower, upper, letter, password in regex.findall(passwords)
)

print(n_valid_passwords)

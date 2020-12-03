import re

INPUT = "input.txt"  # same input

with open(INPUT) as f:
    passwords = f.read()

regex = re.compile(
    r"""
(\d+)-(\d+)  # both indices
\s
(\w):  # letter
\s
(\w+)  # password
""",
    re.VERBOSE,
)


def valid_password(index1, index2, letter, password):
    return (password[index1 - 1] == letter) ^ (password[index2 - 1] == letter)


n_valid_passwords = sum(
    valid_password(int(index1), int(index2), letter, password)
    for index1, index2, letter, password in regex.findall(passwords)
)

print(n_valid_passwords)

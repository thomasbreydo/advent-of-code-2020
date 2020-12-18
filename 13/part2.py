import math

INPUT = "input.txt"


class ModConstraint:
    remainder: int
    mod: int

    def __init__(self, remainder: int, mod: int):
        self.remainder = remainder
        self.mod = mod

    def __str__(self):
        return f"{self.remainder} (mod {self.mod})"


def crt(constraints: list[ModConstraint]):
    """Apply the Chinese Remainder Theorem to simplify a list of modular
    constraints.
    """
    mods = [constraint.mod for constraint in constraints]
    if math.gcd(*mods) != 1:
        raise ValueError("mods must be relatively prime")
    new_mod = math.prod(mods)
    new_remainder = 0
    for constraint in constraints:
        mod = constraint.mod
        remainder = constraint.remainder
        other_mods_prod = new_mod // mod
        new_remainder += remainder * other_mods_prod * pow(other_mods_prod, -1, mod)
    return ModConstraint(new_remainder % new_mod, new_mod)


def main():
    with open(INPUT) as f:
        ids: list[str] = f.read().split("\n")[1].split(",")
    constraint = crt(
        [ModConstraint(-i, int(mod)) for i, mod in enumerate(ids) if mod != "x"]
    )
    print(
        f"The timestamp must be {constraint}, so the answer is {constraint.remainder}"
    )


if __name__ == "__main__":
    main()

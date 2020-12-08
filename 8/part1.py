from typing import Set, List

INPUT: str = "input.txt"

with open(INPUT) as f:
    INSTRUCTIONS: List[str] = f.read().split("\n")

if __name__ == "__main__":
    already_run: Set[int] = set()  # indices of instructions already run
    accumulator: int = 0
    instruction_index: int = 0
    while instruction_index not in already_run:
        already_run.add(instruction_index)
        operation, argument = INSTRUCTIONS[instruction_index].split()
        if operation == "nop":
            instruction_index += 1
        elif operation == "jmp":
            instruction_index += int(argument)
        elif operation == "acc":
            instruction_index += 1
            accumulator += int(argument)

    print(accumulator)

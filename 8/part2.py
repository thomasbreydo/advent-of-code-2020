from typing import List, Set
from part1 import INSTRUCTIONS

INSTRUCTIONS: List[str]


def execute(instructions: List[str]) -> int:
    already_run: Set[int] = set()  # indices of instructions already run
    accumulator: int = 0
    instruction_index: int = 0
    final_instruction_index: int = len(instructions)
    while True:
        already_run.add(instruction_index)
        operation: str
        argument: str
        operation, argument = instructions[instruction_index].split()
        if operation == "nop":
            instruction_index += 1
        elif operation == "jmp":
            instruction_index += int(argument)
        elif operation == "acc":
            instruction_index += 1
            accumulator += int(argument)
        if instruction_index in already_run:
            raise ValueError("instructions cannot loop")
        if instruction_index == final_instruction_index - 1:
            return accumulator


if __name__ == "__main__":
    i: int
    instruction: str
    for i, instruction in enumerate(INSTRUCTIONS):
        operation, argument = instruction.split()
        if instruction == "acc":
            continue
        new_instruction: str = " ".join(
            ("jmp" if instruction == "nop" else "nop", argument)
        )
        new_instructions = INSTRUCTIONS.copy()
        new_instructions[i] = new_instruction
        try:
            print(execute(new_instructions))
        except ValueError:
            continue
        else:
            break

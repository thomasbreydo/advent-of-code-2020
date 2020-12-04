import time
import itertools
import math

N_NUMBERS = 3
INPUT = "input2_from_max.txt"

with open(INPUT) as f:
    report = {int(n) for n in f.readlines()}

start = time.time()
for list_of_n in itertools.permutations(report, N_NUMBERS - 1):
    if (final_n := 2020 - sum(list_of_n)) in report and final_n not in list_of_n:
        print(math.prod(list_of_n) * final_n)
        end = time.time()
        break

print(f"Found in {(end - start) * 1e3} milliseconds.")

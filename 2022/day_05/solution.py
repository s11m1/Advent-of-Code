import copy


def solve(stacks_of_crates: list[str], instructions: str, part: int):
    for instr in instructions.split("\n"):
        ins = instr.split(" ")

        no_of_crates = int(ins[1])
        from_stack = int(ins[3]) - 1
        to_stack = int(ins[5]) - 1

        if part == 1:
            for _ in range(no_of_crates):
                stacks_of_crates[to_stack] += stacks_of_crates[from_stack][-1]
                stacks_of_crates[from_stack] = stacks_of_crates[from_stack][:-1]
        else:
            stacks_of_crates[to_stack] += stacks_of_crates[from_stack][-no_of_crates:]
            stacks_of_crates[from_stack] = stacks_of_crates[from_stack][:-no_of_crates]

    return "".join([x[-1] for x in stacks_of_crates])


if __name__ == '__main__':
    input_data = "data_big.in"

    with open(input_data, 'r') as f:
        stack_all, instructions = f.read().split("\n\n")

    stack = stack_all.splitlines()
    stacks_of_crates = ["" for _ in range(stack[-2].count("["))]

    for line in stack:
        for idx in range(len(stacks_of_crates)):
            symbol_idx = idx * 4 + 1
            if symbol_idx < len(line):
                stacks_of_crates[idx] += line[symbol_idx]

    for idx, val in enumerate(stacks_of_crates):
        stacks_of_crates[idx] = val[:-1].strip()[::-1]

    print("\n-- Part 1: --")
    print(solve(copy.deepcopy(stacks_of_crates), instructions, 1))
    print("\n-- Part 2: --")
    print(solve(copy.deepcopy(stacks_of_crates), instructions, 2))

import copy


def is_position_valid(chamber: set[tuple[int, int]], rock: list[tuple[int, int]]) -> bool:
    for r in rock:
        if r[1] < 0 or r[0] < 0 or r[1] > 6 or r in chamber:
            return False
    return True


def play_tetris(chamber: set[tuple[int, int]], rock_list: list[list[tuple[int, int]]], max_rocks: int) -> int:
    max_height = -1
    instruction_idx = -1
    start_offset = (4, 2)

    for i in range(max_rocks):
        rock_idx = i % 5
        chosen_rock = rock_list[rock_idx]
        rock_position = (max_height + start_offset[0], start_offset[1])

        while True:
            instruction_idx += 1
            instruction = instructions[instruction_idx % len(instructions)]

            #  MOVE RIGHT, LEFT
            new_rock_position = [(rock_position[0] + r[0], rock_position[1] + r[1] + 1) for r in chosen_rock] \
                if instruction == ">" \
                else [(rock_position[0] + r[0], rock_position[1] + r[1] - 1) for r in chosen_rock]

            if is_position_valid(chamber, new_rock_position):
                rock_position = (new_rock_position[0][0], new_rock_position[0][1] - 1) \
                    if rock_idx == 1 \
                    else new_rock_position[0]

            # MOVE DOWN
            new_rock_position = [(rock_position[0] + r[0] - 1, rock_position[1] + r[1]) for r in chosen_rock]

            if is_position_valid(chamber, new_rock_position):
                rock_position = (new_rock_position[0][0], new_rock_position[0][1] - 1) \
                    if rock_idx == 1 \
                    else new_rock_position[0]

            else:
                for r in chosen_rock:
                    chamber.add((rock_position[0] + r[0], rock_position[1] + r[1]))
                    max_height = max(max_height, rock_position[0] + r[0])
                break

    return max_height + 1


if __name__ == '__main__':
    input_data = "data_big.in"
    # input_data = "data_small.in"

    chamber = set()

    rock_list = [[(0, 0), (0, 1), (0, 2), (0, 3)],
                 [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],
                 [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)],
                 [(0, 0), (1, 0), (2, 0), (3, 0)],
                 [(0, 0), (0, 1), (1, 0), (1, 1)]]

    with open(input_data, 'r') as f:
        instructions = f.readline()

    print(instructions)
    print(len(instructions))

    print("\n-- Part 1: --")
    print(play_tetris(copy.deepcopy(chamber), rock_list, 2022))
    print("\n-- Part 2: --")
    print(0)

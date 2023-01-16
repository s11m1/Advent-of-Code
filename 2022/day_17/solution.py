def is_position_valid(chamber: set[tuple[int, int]], rock: list[tuple[int, int]]) -> bool:
    for r in rock:
        if r[1] < 0 or r[0] < 0 or r[1] > 6 or r in chamber:
            return False
    return True


def play_tetris(instructions: str, rock_list: list[list[tuple[int, int]]], max_rocks: int, is_repeated: bool = False) -> list[int]:
    repetition_stats = []
    max_height = -1
    instruction_idx = -1
    chamber = set()
    start_offset = (4, 2)

    for i in range(max_rocks):
        rock_idx = i % 5
        chosen_rock = rock_list[rock_idx]
        rock_position = (max_height + start_offset[0], start_offset[1])

        while True:
            if is_repeated and instruction_idx % (len(rock_list) * len(instructions)) == 0:
                repetition_stats.append(max_height)
                repetition_stats.append(i)
                if len(repetition_stats) >= 6:
                    return repetition_stats[2:]

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

    return [max_height + 1]


def solve_part2(instructions: str, rock_list: list[list[tuple[int, int]]], max_rocks: int):
    repetition_stats = play_tetris(instructions, rock_list, max_rocks, True)

    height_before_repetition = repetition_stats[0]
    rocks_before_repetition = repetition_stats[1]

    height_repetition = repetition_stats[2] - height_before_repetition
    rocks_repetition = repetition_stats[3] - rocks_before_repetition

    rocks_since_repetition = int(max_rocks - rocks_before_repetition)
    repetition_count = int(rocks_since_repetition / rocks_repetition)
    rocks_after_repetition = int(rocks_since_repetition % rocks_repetition)

    rocks_outside_repetition = rocks_before_repetition + rocks_after_repetition

    return repetition_count * height_repetition + play_tetris(instructions, rock_list, rocks_outside_repetition)[0]


if __name__ == '__main__':
    input_data = "data_big.in"

    rock_list = [[(0, 0), (0, 1), (0, 2), (0, 3)],
                 [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],
                 [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)],
                 [(0, 0), (1, 0), (2, 0), (3, 0)],
                 [(0, 0), (0, 1), (1, 0), (1, 1)]]

    with open(input_data, 'r') as f:
        instructions = f.readline()

    print("\n-- Part 1: --")
    print(play_tetris(instructions, rock_list, 2022)[0])
    print("\n-- Part 2: --")
    print(solve_part2(instructions, rock_list, int(1e12)))

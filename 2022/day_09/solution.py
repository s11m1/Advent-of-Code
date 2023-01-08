def move_rope(rope_length: int, input_data: str) -> int:
    tail_path = set()
    knots_all = [[0, 0] for _ in range(rope_length)]
    next_steps = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

    with open(input_data, 'r') as f:
        for line in f.read().splitlines():
            instructions = line.split()
            move_direction = next_steps[instructions[0]]

            for _ in range(int(instructions[1])):
                for i in range(len(knots_all) - 1):
                    head = knots_all[i]
                    tail = knots_all[i + 1]

                    if i == 0:
                        head[0] += move_direction[0]
                        head[1] += move_direction[1]

                    if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1:
                        break

                    elif abs(head[0] - tail[0]) == 2 and abs(head[1] - tail[1]) == 2:
                        tail[0] = int((head[0] + tail[0]) / 2)
                        tail[1] = int((head[1] + tail[1]) / 2)

                    elif abs(head[0] - tail[0]) > 1:
                        tail[0] = int((head[0] + tail[0]) / 2)
                        tail[1] = head[1]

                    elif abs(head[1] - tail[1]) > 1:
                        tail[0] = head[0]
                        tail[1] = int((head[1] + tail[1]) / 2)

                tail_path.add(f"{knots_all[-1]}")
    return len(tail_path)


if __name__ == '__main__':
    input_data = "data_big.in"

    print("\n-- Part 1: --")
    print(move_rope(2, input_data))
    print("\n-- Part 2: --")
    print(move_rope(10, input_data))

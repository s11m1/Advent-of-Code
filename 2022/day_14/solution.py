import copy
from enum import Enum, auto


class Tile(Enum):
    FREE = auto()
    ROCK = auto()
    SAND = auto()


def next_step(cave: list[list[Tile]], x, y) -> tuple[int, int]:
    if y <= len(cave[x]) - 2:
        if cave[x][y + 1] == Tile.FREE:
            return x, y + 1
        if cave[x - 1][y + 1] == Tile.FREE:
            return x - 1, y + 1
        if cave[x + 1][y + 1] == Tile.FREE:
            return x + 1, y + 1
    return x, y


def fall_one_sand_unit(cave: list[list[Tile]], max_height: int) -> int:
    start_position = (500, 0)
    position = start_position

    while True:
        new_position = next_step(cave, position[0], position[1])

        if new_position == start_position or new_position[1] > max_height > -1:
            return 0

        if position == new_position:
            cave[new_position[0]][new_position[1]] = Tile.SAND
            return 1

        position = new_position


def pour_sand(cave: list[list[Tile]], max_height: int, has_bottom: bool) -> int:
    sand_fallen = 0

    if has_bottom:
        for x in range(len(cave)):
            cave[x][max_height + 2] = Tile.ROCK
        max_height = -1

    while True:
        if fall_one_sand_unit(cave, max_height) == 1:
            sand_fallen += 1
        else:
            return sand_fallen


if __name__ == '__main__':
    input_data = "data_big.in"

    guess_max_x = 200
    guess_max_y = 1000
    max_height = 0

    cave = [[Tile.FREE for _ in range(guess_max_x)] for _ in range(guess_max_y)]

    with open(input_data, 'r') as f:
        for line in f.read().splitlines():
            coordinates = [x.split(",") for x in line.split(" -> ")]

            for i in range(len(coordinates) - 1):
                start = coordinates[i]
                end = coordinates[i + 1]
                max_height = max(max_height, int(start[1]), int(end[1]))

                if start[0] == end[0]:
                    for y in range(min(int(start[1]), int(end[1])), max(int(start[1]), int(end[1])) + 1):
                        cave[int(start[0])][y] = Tile.ROCK

                if start[1] == end[1]:
                    for x in range(min(int(start[0]), int(end[0])), max(int(start[0]), int(end[0])) + 1):
                        cave[x][int(start[1])] = Tile.ROCK

    print("\n-- Part 1: --")
    print(pour_sand(copy.deepcopy(cave), max_height, False))
    print("\n-- Part 2: --")
    print(pour_sand(copy.deepcopy(cave), max_height, True) + 1)

def solve_part1(forest: list[list[int]], x: int, y: int) -> int:
    if x == 0 or x == len(forest) - 1 or y == 0 or y == len(forest[0]) - 1:
        return 1

    else:
        curr_tree = forest[x][y]
        curr_x_trees = forest[x]
        curr_y_trees = [row[y] for row in forest]

        if curr_tree > max(curr_x_trees[:y]) \
                or curr_tree > max(curr_x_trees[y + 1:]) \
                or curr_tree > max(curr_y_trees[:x]) \
                or curr_tree > max(curr_y_trees[x + 1:]):
            return 1
    return 0


def solve_part2(forest: list[list[int]], x: int, y: int) -> int:
    visible_tmp = 0
    scenic_score = 1

    for idx in range(x + 1, len(forest)):
        visible_tmp += 1
        if forest[x][y] <= forest[idx][y]:
            break

    scenic_score *= visible_tmp
    visible_tmp = 0

    for idx in range(x - 1, -1, -1):
        visible_tmp += 1
        if forest[x][y] <= forest[idx][y]:
            break

    scenic_score *= visible_tmp
    visible_tmp = 0

    for idx in range(y + 1, len(forest[0])):
        visible_tmp += 1
        if forest[x][y] <= forest[x][idx]:
            break

    scenic_score *= visible_tmp
    visible_tmp = 0

    for idx in range(y - 1, -1, -1):
        visible_tmp += 1
        if forest[x][y] <= forest[x][idx]:
            break

    scenic_score *= visible_tmp
    return scenic_score


if __name__ == '__main__':
    input_data = "data_big.in"

    forest = []

    with open(input_data, 'r') as f:
        for line in f.read().splitlines():
            forest.append([int(x) for x in line])

    visible_trees = 0  # part 1
    max_scenic_score = 0  # part 2

    for x in range(len(forest)):
        for y in range(len(forest[0])):
            visible_trees += solve_part1(forest, x, y)
            max_scenic_score = max(max_scenic_score, solve_part2(forest, x, y))

    print("\n-- Part 1: --")
    print(visible_trees)
    print("\n-- Part 2: --")
    print(max_scenic_score)

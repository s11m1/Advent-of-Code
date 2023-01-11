import string
from typing import TypeAlias

Position: TypeAlias = tuple[int, int]


def bfs(graph: dict[Position, list[Position]], node: Position, backtrack: dict[Position, Position]) -> None:
    queue = [node]
    visited = [node]

    while queue:
        curr = queue.pop(0)
        for neighbor in graph[curr]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
                backtrack[neighbor] = curr


def get_shortest_path(graph, search_from, search_to):
    min_length = len(graph)
    backtrack = {}

    bfs(graph, search_from, backtrack)

    for node in search_to:
        path_length = 0
        curr = node

        while curr != search_from:
            path_length += 1
            if curr in backtrack:
                curr = backtrack[curr]
            else:
                path_length = min_length
                break

        min_length = min(min_length, path_length)

    return min_length


if __name__ == '__main__':
    input_data = "data_big.in"

    elevation = [letter for letter in string.ascii_lowercase]
    heightmap = []

    single_start_node = ()
    all_start_nodes = []
    end_node = ()

    with open(input_data, 'r') as f:
        for line in f.read().splitlines():
            row = []
            for idx, value in enumerate(line):
                if value == "S":
                    single_start_node = (len(heightmap), idx)
                    all_start_nodes.append((len(heightmap), idx))
                    row.append(0)
                elif value == "a":
                    all_start_nodes.append((len(heightmap), idx))
                    row.append(0)
                elif value == "E":
                    end_node = (len(heightmap), idx)
                    row.append(len(elevation) - 1)
                else:
                    row.append(elevation.index(value))
            heightmap.append(row)

    graph_forward = {}
    graph_reversed = {}

    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            graph_forward[(i, j)] = set()

            for offset in [-1, 1]:
                if 0 <= i + offset < len(heightmap) and heightmap[i][j] + 1 >= heightmap[i + offset][j]:
                    graph_forward[(i, j)].add((i + offset, j))
                    if (i + offset, j) not in graph_reversed:
                        graph_reversed[(i + offset, j)] = set()
                    graph_reversed[(i + offset, j)].add((i, j))

                if 0 <= j + offset < len(heightmap[0]) and heightmap[i][j] + 1 >= heightmap[i][j + offset]:
                    graph_forward[(i, j)].add((i, j + offset))

                    if (i, j + offset) not in graph_reversed:
                        graph_reversed[(i, j + offset)] = set()
                    graph_reversed[(i, j + offset)].add((i, j))

    print("\n-- Part 1: --")
    print(get_shortest_path(graph_forward, single_start_node, [end_node]))
    print("\n-- Part 2: --")
    print(get_shortest_path(graph_reversed, end_node, all_start_nodes))

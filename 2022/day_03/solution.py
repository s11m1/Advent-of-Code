import string

if __name__ == '__main__':
    input_data = "data_big.in"

    priority = [letter for letter in string.ascii_letters]
    sum_part1 = 0
    sum_part2 = 0

    with open(input_data, 'r') as f:

        all_lines = f.read().splitlines()

        for line in all_lines:
            mid_point = int(len(line) / 2)

            compartment1 = set([line[i] for i in range(mid_point)])
            compartment2 = set([line[i] for i in range(mid_point, len(line))])

            mistake = compartment1.intersection(compartment2)

            sum_part1 += priority.index(mistake.pop()) + 1

        for i in range(0, len(all_lines), 3):
            rucksack1 = set([l for l in all_lines[i]])
            rucksack2 = set([l for l in all_lines[i + 1]])
            rucksack3 = set([l for l in all_lines[i + 2]])

            common = rucksack1.intersection(rucksack2).intersection(rucksack3)

            sum_part2 += priority.index(common.pop()) + 1

    print("\n-- Part 1: --")
    print(sum_part1)
    print("\n-- Part 2: --")
    print(sum_part2)

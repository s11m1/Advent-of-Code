if __name__ == '__main__':
    input_data = "data_big.in"

    sum_elf = 0
    calories = []

    with open(input_data, 'r') as f:
        for line in f.read().splitlines():
            if line:
                sum_elf += int(line)
            else:
                calories.append(sum_elf)
                sum_elf = 0

    sorted_calories = sorted(calories, reverse=True)

    print("\n-- Part 1: --")
    print(sorted_calories[0])
    print("\n-- Part 2: --")
    print(sum([sorted_calories[x] for x in range(3)]))

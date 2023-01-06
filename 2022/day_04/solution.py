if __name__ == '__main__':
    input_data = "data_big.in"

    complete_overlaps = 0
    partial_overlaps = 0

    with open(input_data, 'r') as f:
        for line in f.read().splitlines():

            sections = line.split(",")
            elf1 = sections[0].split("-")
            elf2 = sections[1].split("-")

            if int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1]):
                complete_overlaps += 1
                partial_overlaps += 1

            elif int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1]):
                complete_overlaps += 1
                partial_overlaps += 1

            elif int(elf1[0]) >= int(elf2[0]) and int(elf1[0]) <= int(elf2[1]):
                partial_overlaps += 1

            elif int(elf1[1]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1]):
                partial_overlaps += 1

    print("\n-- Part 1: --")
    print(complete_overlaps)
    print("\n-- Part 2: --")
    print(partial_overlaps)

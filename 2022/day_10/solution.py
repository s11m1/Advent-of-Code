if __name__ == '__main__':
    input_data = "data_big.in"

    register = [1]
    crt_monitor = ""

    with open(input_data, 'r') as f:
        for line in f.read().splitlines():

            if line.startswith("noop"):
                register.append(register[-1])

            elif line.startswith("addx"):
                value = int(line.split()[1])
                register.append(register[-1])
                register.append(register[-1] + value)

    for cycle in range(240):
        sprite_center = register[cycle]
        sprite_triple = [sprite_center - 1, sprite_center, sprite_center + 1]

        if cycle in range(40, 240 + 1, 40):
            crt_monitor += "\n"
        crt_monitor += "#" if int(cycle % 40) in sprite_triple else "."

    print("\n-- Part 1: --")
    print(sum([cycle * register[cycle - 1] for cycle in range(20, 221, 40)]))
    print("\n-- Part 2: --")
    print(crt_monitor)

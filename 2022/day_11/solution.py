from dataclasses import dataclass
import math, copy


@dataclass
class Monkey:
    items: list[int]
    operation: list[str]
    test_divide: int
    test_true: int
    test_false: int
    inspected_count: int


def update_worry(worry: int, monkey: Monkey) -> int:
    if monkey.operation[1] == "old":
        return worry * worry
    if monkey.operation[0] == "*":
        return worry * int(monkey.operation[1])
    if monkey.operation[0] == "+":
        return worry + int(monkey.operation[1])


def monkey_business(monkeys_gang: list[Monkey], relief: int, rounds: int) -> None:
    base_prime_numbers = math.prod([monkey.test_divide for monkey in monkeys_gang])

    for r in range(rounds):
        for monkey in monkeys_gang:
            while len(monkey.items) > 0:
                worry = monkey.items.pop()
                worry = int(update_worry(worry, monkey) / relief) % base_prime_numbers

                monkey.inspected_count += 1

                if worry % monkey.test_divide == 0:
                    monkeys_gang[monkey.test_true].items.append(worry)
                else:
                    monkeys_gang[monkey.test_false].items.append(worry)


def part_1(monkey_gang: list[Monkey]) -> int:
    monkey_business(monkey_gang, 3, 20)
    sorted_inspected_items = sorted([monkey.inspected_count for monkey in monkey_gang], reverse=True)
    return sorted_inspected_items[0] * sorted_inspected_items[1]


def part_2(monkey_gang: list[Monkey]) -> int:
    monkey_business(monkey_gang, 1, 10000)
    sorted_inspected_items = sorted([monkey.inspected_count for monkey in monkey_gang], reverse=True)
    return sorted_inspected_items[0] * sorted_inspected_items[1]


if __name__ == '__main__':
    input_data = "data_big.in"

    monkey_gang = []

    with open(input_data, 'r') as f:
        for monkey_info in f.read().split("\n\n"):
            lines = monkey_info.split("\n")

            items = lines[1].replace("  Starting items: ", "").split(", ")
            operation = lines[2].replace("  Operation: new = old ", "").split()
            test_divide = int(lines[3].replace("  Test: divisible by ", ""))
            test_true = int(lines[4].replace("    If true: throw to monkey ", ""))
            test_false = int(lines[5].replace("    If false: throw to monkey ", ""))

            monkey_gang.append(Monkey(items=[int(x) for x in items],
                                      operation=operation,
                                      test_divide=test_divide,
                                      test_true=test_true,
                                      test_false=test_false,
                                      inspected_count=0))

    print("\n-- Part 1: --")
    print(part_1(copy.deepcopy(monkey_gang)))
    print("\n-- Part 2: --")
    print(part_2(copy.deepcopy(monkey_gang)))

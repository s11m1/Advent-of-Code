def compare_lists(left: list[int] | int, right: list[int] | int):
    if type(left) == int:
        left = [left]

    if type(right) == int:
        right = [right]

    for idx in range(min(len(left), len(right))):
        if type(left[idx]) == list or type(right[idx]) == list:
            ans = compare_lists(left[idx], right[idx])
            if ans > 0:
                return ans
        elif left[idx] < right[idx]:
            return 1
        elif left[idx] > right[idx]:
            return 2

    if len(left) < len(right):
        return 1
    if len(left) > len(right):
        return 2

    return 0


def partition(packets: list[list[int] | int], min: int, max: int):
    pivot = packets[max]
    i = min - 1

    for j in range(min, max):
        if compare_lists(packets[j], pivot) == 1:
            i += 1
            (packets[i], packets[j]) = (packets[j], packets[i])

    (packets[i + 1], packets[max]) = (packets[max], packets[i + 1])
    return i + 1


def quicksort(packets: list[list[int] | int], min: int, max: int):
    if min < max:
        pi = partition(packets, min, max)
        quicksort(packets, min, pi - 1)
        quicksort(packets, pi + 1, max)


if __name__ == '__main__':
    input_data = "data_big.in"

    divider_packets = ["[[2]]", "[[6]]"]
    all_packets = [eval(divider_packets[0]), eval(divider_packets[1])]

    packets_in_correct_order = 0

    with open(input_data, 'r') as f:
        for idx, line in enumerate(f.read().split("\n\n")):
            parts = line.split()

            left = eval(parts[0])
            right = eval(parts[1])

            all_packets.append(left)
            all_packets.append(right)

            if compare_lists(left, right) == 1:
                packets_in_correct_order += (idx + 1)

    quicksort(all_packets, 0, len(all_packets) - 1)

    idx1 = all_packets.index(eval(divider_packets[0])) + 1
    idx2 = all_packets.index(eval(divider_packets[1])) + 1

    print("\n-- Part 1: --")
    print(packets_in_correct_order)
    print("\n-- Part 2: --")
    print(idx1 * idx2)

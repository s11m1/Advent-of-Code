def find_marker(marker_length: int, signal: str) -> int:
    for i in range(marker_length - 1, len(signal)):
        unique_chars = set()

        for l in range(marker_length):
            unique_chars.add(signal[i - l])

        if len(unique_chars) == marker_length:
            return i + 1


if __name__ == '__main__':
    input_data = "data_big.in"

    with open(input_data, 'r') as f:
        signal = f.readline()

    print("\n-- Part 1: --")
    print(find_marker(4, signal))
    print("\n-- Part 2: --")
    print(find_marker(14, signal))

if __name__ == '__main__':
    input_data = "data_big.in"

    final_score_part1 = 0
    final_score_part2 = 0

    score_posibilities_part1 = {
        "A X": 4,  # Rock - Rock, draw = 1+3
        "A Y": 8,  # Rock - Paper, win = 2+6
        "A Z": 3,  # Rock - Scissors, lose = 3+0

        "B X": 1,  # Paper - Rock, lose = 1+0
        "B Y": 5,  # Paper - Paper, draw = 2+3
        "B Z": 9,  # Paper - Scissors, win = 3+6

        "C X": 7,  # Scissor - Rock, win = 1+6
        "C Y": 2,  # Scissor - Paper, lose = 2+0
        "C Z": 6,  # Scissor - Scissors, draw = 3+3
    }

    score_posibilities_part2 = {
        "A X": 3,  # Rock - Scissors, lose = 3+0
        "A Y": 4,  # Rock - Rock, draw = 1+3
        "A Z": 8,  # Rock - Paper, win = 2+6

        "B X": 1,  # Paper - Rock, lose = 1+0
        "B Y": 5,  # Paper - Paper, draw = 2+3
        "B Z": 9,  # Paper - Scissors, win = 3+6

        "C X": 2,  # Scissor - Paper, lose = 2+0
        "C Y": 6,  # Scissor - Scissors, draw = 3+3
        "C Z": 7,  # Scissor - Rock, win = 1+6
    }

    with open(input_data, 'r') as f:
        for line in f.read().splitlines():
            final_score_part1 += score_posibilities_part1[line]
            final_score_part2 += score_posibilities_part2[line]

    print("\n-- Part 1: --")
    print(final_score_part1)
    print("\n-- Part 2: --")
    print(final_score_part2)

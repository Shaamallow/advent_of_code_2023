# Day 3 Puzzle
# Quite a lot of code but it works and it's understandable

doc = open("input.txt", "r")
lines = doc.readlines()

lines = [line.strip() for line in lines]


def get_positions(lines):
    """
    Return a list of tuples  of positions for the
    characters (not a number or a '.')
    """

    positions = []

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] != "." and not (lines[i][j].isnumeric()):
                positions.append((i, j))

    return positions


def check_around(i, j, n, d):
    """
    Check the 8 positions around the current position

    Return a list of booleans values
    """

    positions = [
        (i - 1, j - 1),
        (i - 1, j),
        (i - 1, j + 1),
        (i, j - 1),
        (i, j + 1),
        (i + 1, j - 1),
        (i + 1, j),
        (i + 1, j + 1),
    ]

    positions_check = []

    for position in positions:
        i_0, j_0 = position

        # verify if the position is valid
        # if not, skip it
        if i_0 < 0 or j_0 < 0:
            continue
        if i_0 >= n or j_0 >= d:
            continue
        if lines[i_0][j_0].isnumeric():
            positions_check.append((i_0, j_0))

    return positions_check


def group_numbers(lines):
    n = len(lines)
    d = len(lines[0])

    validated_numbers = [[False for _ in range(d)] for _ in range(n)]

    characters = get_positions(lines)

    for i, j in characters:
        positions = check_around(i, j, n, d)

        for position in positions:
            i_0, j_0 = position
            validated_numbers[i_0][j_0] = True

    for i in range(n):
        for j in range(d):
            if validated_numbers[i][j]:
                k = j + 1
                while k < d and validated_numbers[i][k]:
                    validated_numbers[i][k] = False
                    k += 1

    return validated_numbers


def puzzle1(lines):
    validated_numbers = group_numbers(lines)

    n = len(lines)
    d = len(lines[0])

    sum = 0

    for i in range(n):
        for j in range(d):
            if validated_numbers[i][j]:
                k = j
                number = ""
                while k < d and lines[i][k].isnumeric():
                    number += lines[i][k]
                    k += 1
                k = j - 1
                while k >= 0 and lines[i][k].isnumeric():
                    number = lines[i][k] + number
                    k -= 1
                sum += int(number)
    return sum


print("Puzzle 1: ", puzzle1(lines))

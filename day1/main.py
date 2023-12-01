# open input.txt file
import re

document = open("input.txt", "r")
lines = document.readlines()


def puzzle_1(lines):
    sum = 0

    for line in lines:
        # find 1st number
        beginNumber = False
        endNumber = False
        n = len(line)
        i = 0
        # small optimization
        digit = ["0", "0"]
        while i < len(line) and not (beginNumber and endNumber):
            char1 = line[i]
            char2 = line[n - 1 - i]
            if char1.isdigit() and not beginNumber:
                beginNumber = True
                digit[0] = char1
            if char2.isdigit() and not endNumber:
                endNumber = True
                digit[1] = char2
            i += 1
        sum += int("".join(digit))
    return sum


def puzzle_2(lines):
    sum = 0

    numbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    regex_patter = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"

    for line in lines:
        matches = re.finditer(regex_patter, line)

        match_list = [match.group(1) for match in matches]
        digit1 = int(
            match_list[0] if match_list[0].isdigit() else numbers[match_list[0]]
        )
        digit2 = int(
            match_list[-1] if match_list[-1].isdigit() else numbers[match_list[-1]]
        )

        sum += 10 * digit1 + digit2
    return sum


print(puzzle_1(lines))
print(puzzle_2(lines))

# DAY 2

doc = open("input.txt", "r")

lines = doc.readlines()

cubes_dict = {"red": 12, "green": 13, "blue": 14}


def check_game(line):
    line = line.strip().split("\n")[0]
    # Get 1 game
    line = line.split(":")
    game_id = line[0].split(" ")[1]
    sets = line[1].split(";")

    for turns in sets:
        turns = turns.split(",")
        turns = [turn.strip() for turn in turns]
        cubes = []  # number of cube i
        colors = []  # color of cube i

        for turn in turns:
            turn = turn.split(" ")
            cubes.append(int(turn[0]))
            colors.append(turn[1])

        for i in range(len(cubes)):
            if cubes[i] > cubes_dict[colors[i]]:
                return 0
    return int(game_id)


def puzzle_1(lines):
    id_sum = 0
    for line in lines:
        id_sum += check_game(line)
    return id_sum


def puzzle_2(lines):
    sum = 0
    for line in lines:
        cubes_dict = {"red": 0, "green": 0, "blue": 0}
        line = line.strip().split("\n")[0]
        # Get 1 game
        line = line.split(":")
        sets = line[1].split(";")

        for turns in sets:
            turns = turns.split(",")
            turns = [turn.strip() for turn in turns]
            cubes = []  # number of cube i
            colors = []  # color of cube i

            for turn in turns:
                turn = turn.split(" ")
                cubes.append(int(turn[0]))
                colors.append(turn[1])

            for i in range(len(cubes)):
                if cubes[i] > cubes_dict[colors[i]]:
                    cubes_dict[colors[i]] = cubes[i]

        sum += cubes_dict["red"] * cubes_dict["green"] * cubes_dict["blue"]

    return sum


print(puzzle_1(lines))
print(puzzle_2(lines))

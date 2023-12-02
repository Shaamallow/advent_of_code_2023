# DAY 2

doc = open("input.txt", "r")

lines = doc.readlines()

cubes_dict = {"red": 12, "green": 13, "blue": 14}
id = 0


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


print(puzzle_1(lines))

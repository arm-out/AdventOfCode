f = open("inputs/day02.txt", "r")
input = f.read().splitlines()

bag = {
    "red": 12,
    "green": 13,
    "blue": 14
}

# setup
games = []
for line in input:
    game = line.split(":")[1]
    game = game.split(";")

    sanitized_game = []
    for pull in game:
        pull = pull.split(",")

        sanitized_pull = [0, 0, 0]
        for colors in pull:
            colors = colors.strip().split(" ")
            match colors[1]:
                case "red":
                    sanitized_pull[0] = int(colors[0])
                case "green":
                    sanitized_pull[1] = int(colors[0])
                case "blue":
                    sanitized_pull[2] = int(colors[0])
        
        sanitized_game.append(sanitized_pull)
    
    games.append(sanitized_game)

# check valid
min_sets = []
for i in range(len(games)):
    game = games[i]
    color_min = [0, 0, 0]
    for pull in game:
        if pull[0] > color_min[0]:
            color_min[0] = pull[0]
        if pull[1] > color_min[1]:
            color_min[1] = pull[1]
        if pull[2] > color_min[2]:
            color_min[2] = pull[2]

    min_sets.append(color_min)

min_power = []
for i in range(len(min_sets)):
    min_power.append(min_sets[i][0] * min_sets[i][1] * min_sets[i][2])

print(sum(min_power))




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
valid = []
for i in range(len(games)):
    game = games[i]
    isValid = True
    for pull in game:
        if pull[0] > bag["red"] or pull[1] > bag["green"] or pull[2] > bag["blue"]:
            isValid = False
            break

    if isValid:
        valid.append(i + 1)

print(sum(valid))


        

